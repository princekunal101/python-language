"""Output_

"""
#programming as a simple calculator

x = int(input("Enter a first number: "))
operator = input("Enter a operator between these: + - * /: ")
y = int(input("Enter a second number: "))

if operator == "+":
    print(x + y)
elif operator == "-":
    print(x - y)
elif operator == "*":
    print(x * y)
elif operator == "/":
    print(x / y)
else:
    print("Invailid operators")