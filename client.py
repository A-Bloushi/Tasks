import requests
url = "http://127.0.0.1:8000/items/"
data = {
    "name": "ff Mug",
    "description": "Ceramic mug",
    "price": 9.99,
    "tax": 0.5
}

response = requests.post(url, json=data)
print(response.status_code)  # 200
print(response.json())       
