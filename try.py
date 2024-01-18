import requests

Base = 'http://127.0.0.1:3000/'

data = [{'likes': 10,'name':'tim','views':10000},
        {'likes': 200,'name':'Web developer Bett','views':2000000},
        {'likes': 10000,'name':'Steph','views':102000}]
headers ={'Content-Type': 'application/json'}

response = requests.put(Base + 'video/3',json=data,headers=headers)
print(response.json())
input()
response = requests.get(Base + 'video/1',json=data,headers=headers)
print(response.json())