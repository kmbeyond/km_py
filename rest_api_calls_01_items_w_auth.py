import requests
import json



#--------Authentication
#token
params = {
	"username": "km",
	"password": "km@1234"
}
headers = {'content-type': 'application/json'}
response = requests.post("http://127.0.0.1:5000/auth", data=json.dumps(params), headers=headers)
#print(json.dumps(response.json(), indent=2))
token = response.json().get('access_token')
print(f"Token: {token}")

headers = {'Authorization': 'JWT '+token+"xxx", 'content-type': 'application/json'}
response = requests.get("http://127.0.0.1:5000/items", headers=headers)
print(json.dumps(response.json(), indent=2))


print("GET items")
response = requests.get("http://127.0.0.1:5000/items")
print(response)
print(json.dumps(response.json(), indent=2))

#print(f"content : {response.content}") # Return the raw bytes of the data payload
#print(f"text : {response.text}") # Return a string representation of the data payload
#print(f"json : {response.json()}") # This method is convenient when the API returns JSON

