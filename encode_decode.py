
import base64

#---base64 encode string
user_name="abcdefgh"
base64.b64encode(user_name.encode('utf-8'))  #returns as bytes
enc_string = base64.b64encode(user_name.encode('utf-8')).decode('utf-8')  #--to get as string

#---decode above string (back to normal string)
base64.b64decode(enc_string)
base64.b64decode(enc_string).decode('utf-8') #--to get as string


EX: Encode file contents
with open('/Users/km/km_pgp_pri.pri', 'r') as f: pri_key = f.read()
enc_string = base64.b64encode(pri_key.encode('utf-8')).decode('utf-8')



#---url safe base64 encode/decode
from base64 import urlsafe_b64encode, urlsafe_b64decode
#from base64 import urlsafe_b64encode as km64e, urlsafe_b64decode as km64d

name_encoded = urlsafe_b64encode(bytes(user_name, 'utf-8'))

#---decode
d_decoded = urlsafe_b64decode(name_encoded)


#---encode json string
import json
s_user = b"""{"name":"abc"}"""
print(f"json: {json.dumps(json.loads(s_user), indent=4)}")
s_encoded = urlsafe_b64encode(s_user)
print(f"JSON encoded -> {s_encoded}")

#---decode
d_decoded = urlsafe_b64decode(s_encoded)
print(f" --> decoded JSON: {d_decoded}")
print(f"to json: \n{json.dumps(json.loads(d_decoded), indent=4)}")

#---encode dictionary
dict_user = {"name":"abc"}
#print(json.dumps(dict_user))
dict_encoded = urlsafe_b64encode(bytes(json.dumps(dict_user), 'utf-8'))
print(f"Dictionary encoded -> {dict_encoded}")

#---decode
d_decoded = json.loads(urlsafe_b64decode(dict_encoded))
print(f" --> decoded back: {d_decoded}")


