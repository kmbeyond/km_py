import requests

print("GET items")
response = requests.get("http://127.0.0.1:5000/items")
print(response)

#print(f"content : {response.content}") # Return the raw bytes of the data payload
#print(f"text : {response.text}") # Return a string representation of the data payload
print(f"json : {response.json()}") # This method is convenient when the API returns JSON

print("POST item")
itm_name="violin3"
itm = {"name": itm_name, "price": 99.99}
#response = requests.post(f"http://127.0.0.1:5000/item/{itm_name}", data=itm)
#print(response)

print("GET items")
response = requests.get("http://127.0.0.1:5000/items")
print(f"{response.json()}")

print(f"GET item: {itm_name}")
response = requests.get(f"http://127.0.0.1:5000/item/{itm_name}")
print(f"{response.json()}")

print(f"PUT item : update {itm_name}")
itm = {"name" : itm_name, "price" : 88.88}
response = requests.put(f"http://127.0.0.1:5000/item/{itm_name}", data=itm)
print(response)

print(f"GET item: {itm_name}")
response = requests.get(f"http://127.0.0.1:5000/item/{itm_name}")
print(f"{response.json()}")

print("GET items")
response = requests.get("http://127.0.0.1:5000/items")
print(f"{response.json()}")