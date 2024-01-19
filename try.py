
import requests

Base = 'http://127.0.0.1:3000/'

data = [{'likes': 10, 'name': 'tim', 'views': 10000},
        {'likes': 200, 'name': 'Web developer Bett', 'views': 2000000},
        {'likes': 10000, 'name': 'Steph', 'views': 102000}]

headers = {'Content-Type': 'application/json'}

# Fix the loop to send individual requests for each item in data
for i in range(len(data)):
    response = requests.put(Base + 'video/' + str(i), json=data[i], headers=headers)
    print(response.json())

# Fix the delete request to use the correct URL
response = requests.delete(Base + 'video/0')
print(response)

# Fix the get request to use the correct URL and remove unnecessary parameters
response = requests.get(Base + 'video/1', headers=headers)
print(response.json())
