import json

emp= [
    {"eid":101,"ename":"A","esal":45000},
    {"eid":102,"ename":"B","esal":450},
    {"eid":103,"ename":"rahul","esal":45}
]

emp_json_st = json.dumps(emp)
print(emp)