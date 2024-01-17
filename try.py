import requests

Base = 'http://127.0.0.1:5555/'

response = requests.put(Base + 'video/1',{'likes':10})
print(response.json())