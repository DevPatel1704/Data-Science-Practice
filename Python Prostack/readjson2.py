import json

fp = open('emp1.json','r')

employee = json.load(fp)

print(employee)