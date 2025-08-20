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

#load data into mongodb collection(table in mysql)
try:
    client = pymongo.MongoClient('mongodb://localhost:27017')
    db = client['dbone']
    users_col = db['users']
    users_col.insert_many(new_users)
    print("Data Inserted in MongoDB")
    
except:
    print("Error while connection to mongoDB")
finally:
    pass
