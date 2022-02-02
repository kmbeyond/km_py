from datetime import datetime, timedelta
import logging, airflow, yaml
from airflow import DAG
from airflow.operators.python_operator import PythonOperator

# logging setup
logging.basicConfig(level=logging.ERROR)
logger = logging.getLogger(__name__)

to_email_address = "km@km.com"
config_yaml_file = "config.yaml"
send_to_bucket = "km-bkt"

#encryption variables
encryption_working_dir = "/tmp/gpg_encryption_home"
encrypted_files_path_prefix = "./gpg_encryption_files/"
secret_prefix = "file-encryption/pgp/"
pgp_service_user_name = "km-gpg-key"
domain = "@km.com"
date_for_file_name = datetime.now().strftime('%Y_%m_%d_%H_%M')
file_name = f"test_{date_for_file_name}.csv"

#decryption variables
decryption_working_dir = "/tmp/gpg_decryption_home"
decrypted_files_path_prefix = "./gpg_encryption_files/"
#decrypted_file_prefix = "decrypted_"

def dag_success_notification(context, **kwargs):
    logger.info("DAG Success")
    print_context(context)


def dag_failure_notification(context, **kwargs):
    logger.info("DAG Failed")
    logger.error("DAG Failed")
    print_context(context)

def print_context(context):
    for k,v in context.items():
        logging.info(f"{k} -> {v}")

def create_test_file(dir_name, file_name):
    import pandas as pd
    data = [(1, 'aa', '2020-01-01'), (2, 'bb', '2021-01-01'), (3, 'cc', '2021-12-01')]
    dataDF = pd.DataFrame(data, columns=['id', 'name', 'login_date'])
    dataDF.to_csv(f"{dir_name}/{file_name}", sep="|", index=False, header=True)


def encrypt_decrypt_files(**kwargs):
    import os

    try:
        encrypt_uncompressed_file(encryption_working_dir, encrypted_files_path_prefix, file_name)
        logger.info("After encrypt:")
        logger.info(os.listdir(encrypted_files_path_prefix))
        #print_dir_iter_contents(encrypted_files_path_prefix)

        logger.info(f"List of files at : {encrypted_files_path_prefix}")
        logger.info(os.listdir(encrypted_files_path_prefix))

        encrypted_file_name = file_name + ".pgp"
        backup_file_name = f"BKP_{file_name}"
        os.system(f"mv {encrypted_files_path_prefix}/{file_name} {encrypted_files_path_prefix}/{backup_file_name}")
        logger.info(f"List of files at : {encrypted_files_path_prefix}")
        logger.info(os.listdir(encrypted_files_path_prefix))

        write_file_to_s3(send_to_bucket, prefix="km_pgp/", stage_loc=encrypted_files_path_prefix,
                         file_name=backup_file_name)
        write_file_to_s3(send_to_bucket, prefix="km_pgp/", stage_loc=encrypted_files_path_prefix,
                         file_name=f"{file_name}.pgp")
        decrypt_file_internal(decryption_working_dir, encrypted_files_path_prefix, encrypted_file_name, encrypted_files_path_prefix)
        #decrypt_file_internal_no_pass(decryption_working_dir, encrypted_files_path_prefix, encrypted_file_name, encrypted_files_path_prefix)
        logger.info("After decrypt:")
        logger.info(f"List of files at : {encrypted_files_path_prefix}")
        logger.info(os.listdir(encrypted_files_path_prefix))
        write_file_to_s3(send_to_bucket, prefix="km_pgp/", stage_loc=encrypted_files_path_prefix,
                         file_name=f"{file_name}")
    except Exception as err:
        logging.info(f"Exception occurred: {err}")
    finally:
        logger.info("Deleting all directories...")
        delete_all_temp_files([ encryption_working_dir,
                            encrypted_files_path_prefix,
                            decryption_working_dir,
                            decrypted_files_path_prefix
                           ])


def encrypt_uncompressed_file(encryption_working_dir, encrypted_files_path_prefix, file_name):
    import os
    if not os.path.exists(encryption_working_dir): os.makedirs(encryption_working_dir)
    if not os.path.exists(encrypted_files_path_prefix): os.makedirs(encrypted_files_path_prefix)

    secret_key_ref = secret_prefix + pgp_service_user_name
    logging.info(f'Getting secrets for : {secret_key_ref}')

    import gnupg
    gpg = gnupg.GPG(gnupghome=encryption_working_dir)
    import boto3
    secretsmanager_conn = boto3.client("secretsmanager", region_name="us-east-1")
    key_data = secretsmanager_conn.get_secret_value(SecretId=f'{secret_key_ref}/publicKey')['SecretString']
    print(f"key_data: {key_data}")
    gpg.import_keys(key_data)
    create_test_file(encrypted_files_path_prefix, file_name)
    with open(encrypted_files_path_prefix + file_name, 'rb') as f:
        status = gpg.encrypt_file(
            f, recipients=[pgp_service_user_name + domain],
            output=encrypted_files_path_prefix + file_name + '.pgp', always_trust=True)
    logger.info("Encrypted: file created: " + encrypted_files_path_prefix + file_name + ".pgp")
    logger.info("COMPLETED: encrypt")


def decrypt_file_internal(decryption_working_dir, encrypted_files_path_prefix, file_name, decrypted_files_path_prefix):
    import os
    if not os.path.exists(decryption_working_dir): os.makedirs(decryption_working_dir)
    if not os.path.exists(decrypted_files_path_prefix): os.makedirs(decrypted_files_path_prefix)

    secret_key_ref = secret_prefix + pgp_service_user_name
    logging.info(f'Getting secrets for : {secret_key_ref}')
    import boto3
    secretsmanager_conn = boto3.client("secretsmanager", region_name="us-east-1")
    secret_key = secretsmanager_conn.get_secret_value(SecretId=secret_key_ref)['SecretBinary']
    print(f"secret_key: {secret_key}")
    secret_passphrase = secretsmanager_conn.get_secret_value(SecretId=f'{secret_key_ref}.passphrase')['SecretString']
    #return secret_key, secret_passphrase
    secrets = secret_key, secret_passphrase

    import gnupg
    gpg = gnupg.GPG(gnupghome=decryption_working_dir)
    gpg.import_keys(secrets[0])

    output_file_name = decrypted_files_path_prefix + file_name[:-4]
    with open(encrypted_files_path_prefix + file_name, "rb") as f:
        status = gpg.decrypt_file(f, passphrase=secrets[1], output=output_file_name)
    print("ok: ", str(status.ok))
    print("status: ", str(status.status))
    print("stderr: ", str(status.stderr))
    if status.ok == True:
        logger.info(f"Decrypted: file created: {output_file_name}")
        os.system(f"cat {output_file_name}")
    else:
        logger.info(f"Decryption FAILED")
    logger.info("COMPLETED: decrypt")


#Print directories, subdirectories & files
def print_dir_iter_contents(sPath):
    import os
    for sChild in os.listdir(sPath):
        sChildPath = os.path.join(sPath,sChild)
        if os.path.isdir(sChildPath):
            from os import listdir
            for file in listdir(sChildPath):
                logger.info(f"-> {file}")
        else:
            print("print_dir_iter_contents=", sChildPath)


def delete_all_temp_files(paths, **kwargs):
    import os
    from os import path
    for path_iter in paths:
        for root, dirs, files in os.walk(path_iter):
            for filename in files:
                remove_temp_file = root + "/" + filename
                if path.exists(remove_temp_file):
                    os.remove(remove_temp_file)
                    print('temp file - ' + remove_temp_file + ' removed')
                else:
                    print(remove_temp_file + ' does not exist!')


def write_file_to_s3(bucket_name, prefix="km_pgp/", stage_loc="/tmp/", file_name=""):
    if file_name=="":
        logging.info("ERROR: No input file name to copy, exiting.")
    else:
        local_file_w_path = stage_loc + file_name
        from os import path
        if path.exists(local_file_w_path):
            logging.info(f"File: {local_file_w_path}; Upload to S3...")
            import boto3, os
            client = boto3.resource('s3')
            logging.info(f"Uploading file to bucket: {bucket_name}")
            client.Bucket(bucket_name).upload_file(stage_loc + file_name, prefix + file_name)
        else:
            logging.warning(f"File not found: {local_file_w_path}")


default_args = {
    'owner': 'km',
    'retries': 3,
    'start_date': airflow.utils.dates.days_ago(2),
    'retry_delay': timedelta(seconds=10),
    'on_failure_callback': dag_failure_notification,
    'on_success_callback': dag_success_notification
}
#    'start_date': datetime.datetime(2021, 01, 01) #airflow.utils.dates.days_ago(2),


with DAG('dag_km_gpg', default_args=default_args, schedule_interval=None, catchup=False, dagrun_timeout=timedelta(minutes=90)) as dag:

    encrypt_decrypt_files = PythonOperator(
        task_id='encrypt_decrypt_files',
        python_callable=encrypt_decrypt_files,
        provide_context=True,
        op_kwargs={
            'to_email_address': to_email_address,
        }
    )
    encrypt_uncompressed_file

