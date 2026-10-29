import requests

response = requests.get("https://ipinfo.io/json").json()

print(f"City: {response['city']}")
print(f"Country: {response['country']}")
print(f"Region: {response['region']}")
