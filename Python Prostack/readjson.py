import json


fp = open("emp.json","r")
emp = json.load(fp)


for name in emp:
    print(name['ename'])
    
    
    
    


# load ->  convert json to python object


# dump -> convert python object to json string