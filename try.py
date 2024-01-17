import requests

Base = 'http://127.0.0.1:5555'

response = requests.get(Base + '/homepage/name/age')
print(response.json())