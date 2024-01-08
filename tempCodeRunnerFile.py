import requests

url = "http://127.0.0.1:5000/"

response = requests.get(url)

if response.status_code == 200:
    # Means OK, everything is fine, we can access the data in different formats, depending on the API's response format.
    # Assuming it's JSON data:
    data = response.json()
    print("Data from the API:")
    print(data)
else:
    print(f"Failed to retrieve data. Status code: {response.status_code}")
