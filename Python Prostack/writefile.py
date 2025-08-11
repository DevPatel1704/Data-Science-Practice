# read data.txt and write into new file abc.txt

fp1 = open('data.txt','r')
data = fp1.read()

fp2 = open("abc.txt",'a') # append write even if it is written already
fp2.write(data)

print("new file created")
fp1.close()
fp2.close()
