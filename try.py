import requests

Base = 'http://127.0.0.1:5555'

response = requests.get(Base + '/video',{'Likes':10})
print(response.json())