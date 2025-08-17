ename = ['rahul','sonia','priya']
# collect all emp name as uppercase in new list

def change_case(ename):
    return ename.upper()

new_ename = list(map(lambda ename:ename.upper(), ename))
    
    
print(ename)
print(new_ename)