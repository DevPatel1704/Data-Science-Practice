import csv
fp = open('users.csv','r')
user_reader = csv.reader(fp)
print(type(user_reader))  # <class '_csv.reader'>
print(user_reader)

users  = list(user_reader)

for user in users[1:]:
    print(user)