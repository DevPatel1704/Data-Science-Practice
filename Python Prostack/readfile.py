fp = open('data.txt','r')

# data = fp.read()
# data = fp.readline(10) # read 10 chars and from first line only 

data = fp.readlines() # read into list format

print(data)


