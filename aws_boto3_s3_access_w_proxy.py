import boto3


from botocore.config import Config
proxy_config = Config(
    proxies={
        'http': 'proxy:port',
        'https': 'proxy:port'
    }
)

s3_proxy = boto3.resource('s3', config=proxy_config)

