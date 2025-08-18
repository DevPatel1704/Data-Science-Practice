
try:
    a = int(input("Enter number : "))
    b = int(input("Enter number : "))

    print(a/b)
    
# except ValueError as err:
#     print(err)
    
# except ZeroDivisionError as err:
#     print(err)
    
    
except (ValueError,ZeroDivisionError) as err:
    print(err)

print("GM")