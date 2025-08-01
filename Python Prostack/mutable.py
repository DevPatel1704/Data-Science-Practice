ename = ["rahul","b","c"]
eids={1,2,3,3}
emp={
    'eid':101,
    'ename':"rahul"
}
ba=bytearray([10,20,30,100])

print(type(ename))
print(type(eids))
print(type(emp))
print(type(ba))

ename[0] = "rahul gandhi"
print(ename)
eids.add(200)
print(eids)

emp['lox']="hello"
print(emp)