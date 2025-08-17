import json,csv,requests

response = requests.get('https://jsonplaceholder.typicode.com/users')
users = response.json()
# print(type(users)) #list

#Treansform user's ata for csv file
employees = []
for user in users:
    employees.append((user['id'],user['username'],user['phone'],user['address']['city']))



# Write/load user data into new json file user.json

fp1 = open('user.json','w')
json.dump(users,fp1)
print("new user.json file created")

# Write user data into new csv file -user.csv 

fp2 = open('user.csv','w')
cw = csv.writer(fp2)
cw.writerow(['eid','ename','phoneno','city'])
cw.writerows(employees)
print("new csv file created")

fp1.close()
fp2.close()