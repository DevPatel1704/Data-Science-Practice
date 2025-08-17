from functools import reduce 

numbers  = [12,3,4,4,5,6] # some of the n number s

sum  = reduce(lambda a,b:a+b,numbers)
print(sum)