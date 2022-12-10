import math 

def calculator(): 
    print("Welcome to the Python Calculator App!") 
    num1 = float(input("Enter your first number: ")) 
    op = input("Enter an operator: ") 
    num2 = float(input("Enter your second number: ")) 

    if op == "+": 
        print(num1 + num2) 

    elif op == "-": 
        print(num1 - num2) 

    elif op == "*": 
        print(num1 * num2) 

    elif op == "/": 
        print(num1 / num2) 

    elif op == "**": 
        print(num1 ** num2) 

    elif op == "sqrt": 
        print(math.sqrt(num1)) 

calculator()