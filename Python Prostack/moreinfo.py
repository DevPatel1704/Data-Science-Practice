fp = open('data.txt','r')


# to know about file pointer information
print(fp.name)
print(fp.mode)
print(fp.readable())
print(fp.writable())
print(fp.closed)
fp.close()
print(fp.closed)


