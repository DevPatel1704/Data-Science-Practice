import json

fp = open('emp1.json','r')

employee = json.load(fp)

print(employee)

## Want to print only male employes

for emp in employee:
    if emp['gender'] == "Male":
        print("Employee Id",emp['eid'],"and emp of Name:",emp['name'])