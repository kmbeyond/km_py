import requests
import json

print("GET items")
response = requests.get("http://127.0.0.1:5000/items")
print(response)
print(json.dumps(response.json(), indent=2))

#print(f"content : {response.content}") # Return the raw bytes of the data payload
#print(f"text : {response.text}") # Return a string representation of the data payload
#print(f"json : {response.json()}") # This method is convenient when the API returns JSON

itm_name="violin4"
print(f"POST item - add item: {itm_name}")
itm = {"name": itm_name, "price": 999.99}
response = requests.post(f"http://127.0.0.1:5000/item/{itm_name}", data=itm)
#print(response)

print("GET all items")
response = requests.get("http://127.0.0.1:5000/items")
print(json.dumps(response.json(), indent=2))

print(f"GET only item: {itm_name}")
response = requests.get(f"http://127.0.0.1:5000/item/{itm_name}")
print(json.dumps(response.json(), indent=2))

itm_name="violin5"
print(f"PUT item : update {itm_name}")
itm = {"name" : itm_name, "price" : 99.99}
response = requests.put(f"http://127.0.0.1:5000/item/{itm_name}", data=itm)
print(json.dumps(response.json(), indent=2))

print("GET items")
response = requests.get("http://127.0.0.1:5000/items")
print(json.dumps(response.json(), indent=2))

