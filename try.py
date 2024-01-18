import requests

Base = 'http://127.0.0.1:3000/'


headers = {'Content-Type': 'application/json'}

response = requests.put(Base + 'video/1', {'likes': 10,'name':'tim','views':10000}, headers=headers)

print(response.json())
