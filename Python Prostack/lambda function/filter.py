ename = ['rahul','sonia','priya']
# collect all emp name as uppercase in new list

def change_case(ename):
    return ename.upper()

new_ename = list(map(change_case, ename))
    
    
print(ename)
print(new_ename)

'''
map() - to create new seq based on condition
filter() - to filter values/elements of given sequence
           based on condition
'''