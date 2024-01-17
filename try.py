import requests

Base = 'http://127.0.0.1:5555'

response = requests.post(Base + '/homepage')
print(response.json())