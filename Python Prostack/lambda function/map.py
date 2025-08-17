# python inbuild function
# map()
# filter()

price = [10,12,300,340]

# increase every product price +plus one
#output 
# [11,13,301,341]

# new_price = []

# for p in price:
#     new_price.append(p+1)
    
# print(price)
# print(new_price)


# map : execute provided function for every element of sequence 
def addplus(p):
    return p+1

obj = map(addplus, price)
new_price = list(obj)
print(price)
print(new_price)