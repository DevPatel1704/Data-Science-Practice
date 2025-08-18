a = None
b = None

try:
    a = int(input("Enther first number : "))
    b = int(input("Enther second number : "))

    print(a/b)
    
except ZeroDivisionError as err:
    print(err)
    
print("GM")