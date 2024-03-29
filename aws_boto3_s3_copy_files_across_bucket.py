import boto3

s3 = boto3.resource('s3', region='us-east-2')
s3 = boto3.resource('s3', region='us-east-2')

# logging setup
import logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


def archive_data(bucket_name_src, file_dir_prefix, archive_bucket_name, archive_customer_prefix, **kwargs):
    bucket1 = s3.Bucket(bucket_name_src)
    #kms_key = kwargs['archive-kms-key-arn']
    for file in bucket1.objects.filter(Prefix=file_dir_prefix):
        logger.info(f"File : {bucket_name_src}/{file.key}")
        logger.info(f" --> {archive_bucket_name}/{file.key}")
        s3.meta.client.copy(
            {'Bucket': bucket_name_src, 'Key': file.key},
            archive_bucket_name,
            f"{archive_customer_prefix}/{file.key}"
            #,ExtraArgs={'ServerSideEncryption': 'aws:kms', 'SSEKMSKeyId': kms_key}
        )


