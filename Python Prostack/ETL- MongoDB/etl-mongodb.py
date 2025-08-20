import requests,mysql.connector, pymongo
# extract from source -Rest API/cloud
res_data = requests.get('https://jsonplaceholder.typicode.com/users')

users = res_data.json()

# transform data for mongodb data 

new_users = []

for user in users:
    new_users.append({'uid':user['id'],
                      'uname':user['username'],
                      'city':user['address']['city']
                      })

print(new_users)

#load data into mongodb conncetion
try:
    client = pymongo.MongoClient()
    db = client['']
except:
    pass
finally:
    pass
