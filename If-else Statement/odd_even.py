"""Output_

Enter a number: ...
... is even
It belongs table of 2

... is odd
It does not belongs table of 2
"""
#get a number 
a = int(input("Enter a number: "))

if a % 2 == 0:
    print(str(a) + " is even")
    print("It belongs table of 2")
else:
    print(str(a) + " is odd")
    print("It does not belongs table of 2")