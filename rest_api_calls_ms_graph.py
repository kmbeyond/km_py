import requests
import json

TENANT_ID = ''
APPL_CLIENT_ID = ''
CLIENT_SECRET=''
username=''
password=''

#-----Token
print("Acquire token")
token_url = f"https://login.microsoftonline.com/{TENANT_ID}/oauth2/v2.0/token"
params = {
  'grant_type': 'password',
  'client_id': APPL_CLIENT_ID,
  'client_secret': CLIENT_SECRET,
  'scope': 'https://graph.microsoft.com/.default',
  'username': username,
  'password': password
}

response = requests.post(token_url, data=params)
print(f"Response JSON: \n{json.dumps(response.json(), indent=4)}")
print(f"Resp content: {response.content}")
token = ""
token = response.json().get('access_token')
print(f"Token: {token}")
if token == "" or token == None:
  print("INVALID TOKEN")
  #return {"status": "failed", "error_code": "PPA-100", "error_message": "Blank/invalid Token"}
  raise ValueError('Failed to get token')

##https://jwt.io/

#-----SendEmail

to_email = "email@gmail.com"
email_subject = 'TEST email using MS Graph API'
email_body_html = f"""TEST PPA email body<br><br><h2>HTML table</h2><table border="1" cellspacing=0><tr><th>header1</th><th>header2</th><tr><td>abcdef</td><td align=center>1.5</td></tr></table><br><br><br>
        <br><br>++ : The date-times are in UTC.<br><strong>NOTE:</strong> This message was sent from an unmonitored email address. Please do not respond to this message.
"""
email_body_text = """
welcome to email
Thanks"""

headers = {'Authorization': 'Bearer '+token, 'content-type': 'application/json'}
message_data = {
  "message": {
    "subject": email_subject,
    "body": {
      "contentType": "HTML",
      "content": email_body_html
    },
    "toRecipients": []
  }
}
#"toRecipients": [ {"emailAddress": {"address": to_email}} ]

to_email = "email1@gmail.com,email2@gmail.com"
def add_email_addresses(message_data, to_email):
  for email in to_email.split(','):
    email_dict = {"emailAddress": {"address": email.strip()}}
    print(f"Add email address: {email.strip()}")
    message_data['message']['toRecipients'].append(email_dict)
  return message_data


message_data = add_email_addresses(message_data, to_email)
#print(f"Message Dict: {json.dumps(message_data, indent=4)}")

response = requests.post("https://graph.microsoft.com/v1.0/me/sendMailx",  data=json.dumps(message_data), headers=headers)

print(f"Resp content: {response.text}")
if response.text == "":
  print("success")
else:
  print(f"error:{str(response)}")
  print(f"error code:{str(response.json().get('error').get('code'))}")
  print(f"error message:{str(response.json().get('error').get('message'))}")
  print({"status": "failed", "error_code": f"{str(response.json()['error']['code'])}",
         "error_message": f"{str(response.json()['error']['message'])}"})



