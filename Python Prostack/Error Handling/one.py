try:
    fp = open('data.txt','r')
    data = fp.read()

    print(data)

except FileNotFoundError as err:
    print(err)
    
    
print("GM")
print("GA")