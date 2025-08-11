#json.loads() -- >convers json str to py object

import json

emp_json_str= '''[
    {"eid":101,"ename":"A","esal":45000},
    {"eid":102,"ename":"B","esal":450},
    {"eid":103,"ename":"rahul","esal":45}
]
'''

emp = json.loads(emp_json_str)
print(type(emp))
print(emp)

for x in emp:
    print(x['ename'])