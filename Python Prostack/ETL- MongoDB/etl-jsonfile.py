import requests,mysql.connector, pymongo, json
# extract from source -Rest API/cloud
res_data = requests.get('https://jsonplaceholder.typicode.com/users')
users = res_data.json()

# transform data for json data 
new_users = []

for user in users:
    new_users.append({'uid':user['id'],
                      'uname':user['username'],
                      'city':user['address']['city']
                      })

print(new_users)

#load data into json file - users.json

fp = None


try:
    fp = open('users.json','w')
    json.dump(new_users,fp)
    print("New Users Json file created")
except:
    pass

finally:
    fp.close()