import requests,mysql.connector
# extract from source -Rest API/cloud
res_data = requests.get('https://jsonplaceholder.typicode.com/users')

users = res_data.json()

# transform for myaql tables

new_users = []

for user in users:
    new_users.append((user['id'],user['username'],user['email'],user['address']['city'],user['phone']))
  
  

# load data into mysql table   
dbcon = None
cursor = None

try:
    dbcon = mysql.connector.connect(host='localhost',user='root',password='root',database='dbone')
    cursor = dbcon.cursor()
    sql_st = '''
             insert into users(uid,uname,email,city,phone) 
             values(%s,%s,%s,%s,%s)
    '''
    cursor.executemany(sql_st,new_users)
    dbcon.commit()
    print("data inserted")
    
except mysql.connector.Error as err:
    print(err)

finally:
    if dbcon is not None:
        dbcon.close()


