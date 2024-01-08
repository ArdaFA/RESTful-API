import requests

url = "http://127.0.0.1:5000/cars/2"
response = requests.get(url)

if response.status_code == 200:
    data = response.json()
    print("Data from the API:")
    print("Name:", data["name"])
    print("Model:", data["model"])
else:
    print(f"Failed to retrieve data. Status code: {response.status_code}")
