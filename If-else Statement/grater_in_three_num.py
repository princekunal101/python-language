"""Output_

Enter a first number: ...
Enter a second number: ...
Enter a third number: ...
... is gratter number
"""
#get three number from users

a = int(input("Enter a first number: "))
b = int(input("Enter a second number: "))
c = int(input("Enter a theird number: "))

if a > b and a > c:
    print(str(a) + " is gratter number")
elif b > a and b > c:
    print(str(b) + " is gratter number")
else:
    print(str(c) + " is gratter number")
