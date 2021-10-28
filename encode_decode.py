import json
from base64 import urlsafe_b64encode as km64e, urlsafe_b64decode as km64d


#---encode string
user_name="abcdefgh"
name_encoded = km64e(bytes(user_name, 'utf-8'))
print(f"{user_name} is encoded -> {name_encoded}")

#---decode
d_decoded = km64d(name_encoded)
print(f" --> decoded back: {d_decoded}")


#---encode json string
s_user = b"""{"name":"abc"}"""
print(f"json: {json.dumps(json.loads(s_user), indent=4)}")
s_encoded = km64e(s_user)
print(f"JSON encoded -> {s_encoded}")

#---decode
d_decoded = km64d(s_encoded)
print(f" --> decoded JSON: {d_decoded}")
print(f"to json: \n{json.dumps(json.loads(d_decoded), indent=4)}")

#---encode dictionary
dict_user = {"name":"abc"}
#print(json.dumps(dict_user))
dict_encoded = km64e(bytes(json.dumps(dict_user), 'utf-8'))
print(f"Dictionary encoded -> {dict_encoded}")

#---decode
d_decoded = json.loads(km64d(dict_encoded))
print(f" --> decoded back: {d_decoded}")


