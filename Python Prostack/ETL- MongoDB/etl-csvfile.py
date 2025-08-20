import requests,mysql.connector, pymongo, json, csv
# extract from source -Rest API/cloud
res_data = requests.get('https://jsonplaceholder.typicode.com/users')
users = res_data.json()

# transform data for csv data 
new_users = []

for user in users:
    new_users.append((user['id'],user['username'],user['email']))

print(new_users)

# Load the data 
fp = None

try:
    fp = open('users.csv','w',newline='')
    cw = csv.writer(fp)
    cw.writerow(['userId','userName','email'])
    cw.writerows(new_users)
    print("New CSV file created")
except:
    print("unable created new CSV file")
finally:
    fp.close()