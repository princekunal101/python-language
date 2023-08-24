"""Output_

The first num is: 5
The second num is: 9
Here adding as a string so:
59
Converting string to int then Output is:
14
"""
#sum of two numbers

a = input("The first num is: ")
b = input("The second num is: ")

print("Here adding as a string so: ")
#here the a and b are the string so Output is as string
sum = a + b
print(sum)
#ab

print("Converting string to num then Output is: ")
#we need to convert string to int
sum = int(a) + int(b)
print(sum)
#a+b