import requests

res_data = requests.get('https://jsonplaceholder.typicode.com/users')

users = res_data.json()

# transform for myaql tables

new_users = []

for user in users:
    new_users.append((user['id'],user['username'],user['email'],user['address']['city'],user['phone']))
    
print(new_users)

