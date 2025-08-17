import csv
fp = open('users.csv','r')
user_reader = csv.reader(fp)
print(type(user_reader))  # <class '_csv.reader'>

users  = list(user_reader)
print(users)

# excluding csv header by list slicing
print(users[1:])

# Print usrer names 
for users in users[1:]:
    print(users[1])
    
