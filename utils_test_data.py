from datetime import datetime, timedelta
import logging, random, string
import boto3, os
from os import path

# logging setup
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# snowflake connection
##snowflake_hook = SnowflakeHook(snowflake_conn_id=config['snowflake_conn_id'], autocommit=False)
##cs = snowflake_hook.get_cursor()

def get_date_yyyy_mm_dd(days_back=0):
    return (datetime.now() + timedelta(days=days_back)).strftime('%Y-%m-%d')

def get_datetime_formatted(days_back=0):
    # datetime format: YYYY-MM-DD HH.MI.SS.FFFFFF
    return (datetime.now() + timedelta(days=days_back)).strftime('%Y-%m-%d %H.%M.%S.%f')

def get_datetime_from_datetime(input_datetime, days_back=0):
    # Input & output datetime format: YYYY-MM-DD HH.MI.SS.FFFFFF
    return (datetime.strptime(input_datetime, '%Y-%m-%d %H.%M.%S.%f') + timedelta(days=days_back)
            ).strftime('%Y-%m-%d %H.%M.%S.%f')

def get_datetime_formatted_string(days_back=0):
    return (datetime.now() + timedelta(days=days_back)).strftime('%Y_%m_%d_%H_%M_%S')


def get_random_datetime_formatted(days_back=0):
    # datetime format: YYYY-MM-DD HH.MI.SS.FFFFFF
    # return datetime.now().strftime( '%Y-%m-%d %H.%M.%S.%f' )
    return (datetime.now() + timedelta(days=days_back, hours=random.randint(1, 23), minutes=random.randint(1, 59))
            ).strftime('%Y-%m-%d %H.%M.%S.%f')


#def get_random_datetime_from_datetime_formatted_001(input_datetime, min_days, max_days, from_current=-1):
    # Input & output datetime format: YYYY-MM-DD HH.MI.SS.FFFFFF
#    rand_days = random.randint(min_days, max_days) * from_current
#    return (datetime.strptime(input_datetime, '%Y-%m-%d %H.%M.%S.%f') + timedelta(days=rand_days,
#                                                                                hours=random.randint(1, 23),
#                                                                                minutes=random.randint(1, 59)
#                                                                                )
#            ).strftime('%Y-%m-%d %H.%M.%S.%f')


def gen_random_string(type, num_chars=10):
    if type == "NUM":
        char_set = string.digits
    elif type == "ALPHA":
        char_set = string.ascii_uppercase + string.ascii_lowercase
    else:
        char_set = string.ascii_uppercase + string.ascii_lowercase + string.digits
    s_random_chars = ''.join(random.sample(char_set * num_chars, num_chars))
    return s_random_chars


def gen_random_from_list(list_lookup):
    return list_lookup[random.randint(0, len(list_lookup) - 1)]


def gen_random_from_list2(list_lookup, already_picked_list, trials=3):
    # Does not return duplicates
    while trials > 0:
        rand_item = random.randint(0, len(list_lookup) - 1)
        if rand_item in already_picked_list:
            trials -= 1
        else:
            #already_picked_list.append(rand_item)
            return rand_item
    return ""


def get_random_item_from_dict(data_dict):
    dict_keys = list(data_dict)
    # dict_keys = list(data_dict.keys())
    dict_keys_index = random.randint(0, len(dict_keys) - 1)
    return [dict_keys[dict_keys_index], data_dict[dict_keys[dict_keys_index]]]


def get_random_item_from_dict2(data_dict, already_picked_list, trials=3):
    # returns list [key, val]
    # Does not return duplicates; "" if no item
    dict_keys = list(data_dict)
    # dict_keys = list(data_dict.keys())
    while trials > 0:
        dict_keys_index = random.randint(0, len(dict_keys) - 1)
        if dict_keys_index in already_picked_list:
            trials -= 1
        else:
            already_picked_list.append(dict_keys_index)
            return [dict_keys[dict_keys_index], data_dict[dict_keys[dict_keys_index]]]
    return ["", ""]


def read_lookup_data_file(file_path, file_name='test_data_customers_list.csv'):
    file_with_path = file_path + file_name
    fp = open(file_with_path, 'r')
    with fp:
        lines = fp.readlines()
    # print(lines)
    fp.close()
    return {
        itm.split(',')[6] : itm.split(',') for itm in lines[1:]
    }


def generate_test_data_km1(rows=10):
    data_rows = []
    lookup_list = ['aaa', 'ccc', 'ggg', 'yyy', 'zzz']
    lookup_dict = {"a": "aaa", "b": "bbb", "c": "ccc", "d": "ddd"}

    for i in range(rows):
        dict_itm = get_random_item_from_dict(lookup_dict)
        data_rows.append(",".join([
            get_date_yyyy_mm_dd(),
            get_date_yyyy_mm_dd(0).ljust(15),
            get_date_yyyy_mm_dd(-1).ljust(10),
            get_date_yyyy_mm_dd(random.randint(10, 20)*-1),  # back date
            get_date_yyyy_mm_dd(random.randint(10, 20)*1),  # future date
            gen_random_from_list(lookup_list).ljust(10),
            dict_itm[0].ljust(10),
            dict_itm[1].ljust(10),
            str(round(random.randint(100000, 1000000) / 100, 2)).rjust(13, '0'), # 1111.11
            str(random.randint(100000, 1000000)).rjust(13, '0'),  #sal:123456
            gen_random_string(type="NUM", num_chars=5).ljust(10),
            gen_random_string(type="ALPHA", num_chars=7).ljust(10),
            gen_random_string(type="ANY", num_chars=10).ljust(10),
            'S'.ljust(20, ' '),
            "*"
        ]))
    return data_rows

def generate_test_data_km2(cust_data, delimiter=","):
    return [
        delimiter.join([
            k.ljust(10),
            v[1].ljust(10),
            "*"
        ]) for k, v in cust_data.items()
    ]


def write_list_to_s3(file_name, data_list, bucket_name, prefix, data_delimiter):
    file_name = file_name + (".txt" if data_delimiter == "" else ".csv")
    import pandas as pd
    data_df = pd.DataFrame(data_list)
    #data_df.to_csv(file_name, index=False, header=False)

    logging.info(f"Upload to S3: {bucket_name}{prefix}{file_name}")
    import io, csv
    csv_buffer = io.StringIO()
    data_df.to_csv(csv_buffer, index=False, header=False)
    client = boto3.resource('s3')
    client.Object(bucket_name, prefix+file_name).put(Body=csv_buffer.getvalue())


def write_list_to_s3_stage(file_name, data_list, bucket_name, prefix, data_delimiter):
    final_data = "\n".join(data_list)
    # logger.info("\nData generated: \n" + final_data)
    stage_loc = "/tmp/"
    file_name = file_name + (".txt" if data_delimiter == "" else ".csv")
    local_file_w_path = stage_loc + file_name
    with open(local_file_w_path, 'w') as file:
        file.write(final_data)

    logging.info("Upload to S3...")
    upload_to_s3(bucket_name, prefix, file_name, stage_loc)

    if path.exists(local_file_w_path):
        os.remove(local_file_w_path)
        logging.info("Deleted file: " + local_file_w_path)
    else:
        logging.warning("Local file not found: " + local_file_w_path)


def upload_to_s3(bucket_name, prefix, file_name, local_path):
    client = boto3.resource('s3')
    logging.info(f"Uploading file to bucket: {bucket_name}")
    client.Bucket(bucket_name).upload_file(local_path + file_name, prefix + file_name)



def generate_test_data(task_id, **kwargs):
    #bucket_name = config['test_data_bucket_name']
    #prefix = config['test_data_prefix']
    #data_delimiter = Variable.get("test_data_delimiter", "")
    bucket_name = "kmbkt"
    prefix = "test_data/"
    data_delimiter = ""

    os.environ['AIRFLOW_HOME'] = 'C:\\Users\\km\\PycharmProjects\\airflow-dags'
    lookup_files_path = os.path.join(os.getenv('AIRFLOW_HOME', '~/airflow'), 'KM', '')
    #lookup_files_path = os.path.join(os.getenv('AIRFLOW_HOME', '~/airflow'), 'dags', 'KM', '')
    lookup_file_cust = 'test_data_customers_list.csv'

    cust_data = read_lookup_data_file(lookup_files_path, file_name=lookup_file_cust)
    #for rec in cust_data: logging.info(f"{rec} -> {cust_data[rec]}")

    data_class = "test_data"
    file_name = f"{datetime.now().strftime('%Y%m%d%H%M%S')}_test_data"
    data_list = generate_test_data_km2(cust_data, data_delimiter)
    #for rec in data_list: logging.info(f"{rec}")
    write_list_to_s3(file_name, data_list, bucket_name, prefix, data_delimiter)

    logging.info("Complete")


generate_test_data("km_task")
