import boto3
from botocore.config import Config
import logging

# logging setup
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


def km_send_email(to_email, subject, body):
    try:
        config_ses = Config(
            retries={
                'max_attempts': 2,
                'mode': 'standard'
            }
        )
        ses_client = boto3.client("ses", region_name="us-east-2",
                                  #aws_access_key_id=access_key,
                                  #aws_secret_access_key=secret_key,
                                  config=config_ses)
        # endpoint_url="email-smtp.us-east-1.amazonaws.com",
        print("verified addresses:" + str(ses_client.list_verified_email_addresses()))
        response = ses_client.send_email(
            Destination={
                "ToAddresses": to_email,
            },
            Message={
                "Body": {
                    "Html": {
                        "Charset": "UTF-8",
                        "Data": body,
                    }
                },
                "Subject": {
                    "Charset": "UTF-8",
                    "Data": subject,
                },
            },
            Source='kmbeyond@gmail.com'
        )
        print('Response details:')
        for k, v in response.items():
            print(k, '->', v)
        print("SES Success")
    except Exception as err:
        print(f"Failed to send using SES: {err}")
    else:
        print(f"Email sent! MessageId={response['MessageId']}")


def main():
    to_email=['kmbeyond@gmail.com']
    body='<h3>Email from SES</h3>'
    subject='Email from SES'
    km_send_email(to_email, subject, body)

if __name__ == "__main__":
    main()