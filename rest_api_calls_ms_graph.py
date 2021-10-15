import requests
import json

#TENANT_ID_NOISED = ''
#print(TENANT_ID_NOISED[7:])
#TENANT_ID_NOISED = ''
#print(TENANT_ID_NOISED[7:-7])

TENANT_ID = ''
APPL_CLIENT_ID = ''
client_secret=''
username=''
password=''

#-----Token
print("Acquire token")
token_url = f"https://login.microsoftonline.com/{TENANT_ID}/oauth2/v2.0/token"
params = {
  'grant_type': 'password',
  'client_id': APPL_CLIENT_ID,
  'client_secret': client_secret,
  'scope': 'https://graph.microsoft.com/.default',
  'username': username,
  'password': password
}

response = requests.post(token_url, data=params)
##print(f"Response: {response}")
#print(f"Resp content: {response.content}")
token=""
token = response.json().get('access_token')
print(f"Token: {token}")
##https://jwt.io/

#-----SendEmail
to_email_address=""
email_subject='TEST PPA email'
email_body="""TEST PPA email body<br><br><h2>HTML table</h2><table border="1"><tr><th>header</th><tr><td>abcdef</td></tr></table><br><br><br>
"""
email_msg_footer="""<br><br><br><strong>NOTE:</strong> This message was sent from an unmonitored email address. Please do not respond to this message.
"""

headers = {'Authorization': 'Bearer '+token, 'content-type': 'application/json'}
message_data = {
  "message": {
    "subject": email_subject,
    "body": {
      "contentType": "HTML",
      "content": email_body+email_msg_footer
    },
    "toRecipients": [ {"emailAddress": {"address": to_email_address}} ]
  }
}
print(f"message_data: {message_data}")
to_email_address2_dict = {"emailAddress": {"address": ""}}
print(f"Add emailAddress: {to_email_address2_dict}")
message_data['message']['toRecipients'].append(to_email_address2_dict)

response = requests.post("https://graph.microsoft.com/v1.0/me/sendMail",  data=json.dumps(message_data), headers=headers)
#print(f"Resp content: {response.content}")


