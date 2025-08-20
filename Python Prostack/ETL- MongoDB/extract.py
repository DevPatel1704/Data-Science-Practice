import requests

res_data = requests.get('https://jsonplaceholder.typicode.com/users')

status_code = res_data.status_code
users = res_data.json()
print(type(users))
print(status_code)