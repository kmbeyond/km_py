import boto3
from botocore.config import Config
import logging
import json

# SETUP:
#User must be authorized to use SNS - Ex: add AmazonSNSFullAccess policy to user

# logging setup
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

def send_sns_message(account_num, region_name, topic_name, subject, message):
    topic_arn='arn:aws:sns:'+region_name+':'+account_num+':'+topic_name
    sns = boto3.resource('sns',
        endpoint_url='https://sns.'+region_name+'.amazonaws.com',
        region_name=region_name
        #aws_access_key_id=access_key,
        #aws_secret_access_key=secret_key
    )
    topic = sns.Topic(topic_arn)
    # publish to SNS
    #response = topic.publish(
    #    Subject=subject,
    #    Message=json.dumps({'default': message}),
    #    MessageStructure='json'
    #)
    response = topic.publish(
        Subject=subject,
        Message=message
    )
    ## using client (low level) & direct SMS
    #sns_client = boto3.client('sns')
    #sns_client.publish(PhoneNumber="+1234567890", Message="testing simple text")


def main():
    region_name = 'us-east-1'
    topic_name = ''
    account_num = ''
    subject = "test subject"
    message = '{0}'.format("simple test message")
    send_sns_message(account_num, region_name, topic_name, subject, message)

if __name__ == "__main__":
    main()
