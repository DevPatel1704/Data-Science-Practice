# program to read app.txt file and print data

fp = None
try:
    fp = open('abc.txt','r')
    data = fp.read()
    print(data)
except FileNotFoundError as err:
    print("File not found so app.txt is executed")
    fp=open('app.txt','r')
    data=fp.read()
    print(data)

finally:
    print("this will be executed whether error is not or there")
    fp.close()