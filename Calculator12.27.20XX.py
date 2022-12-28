print("Enter the first number")
num1 = input()
print("Enter the second number")
num2 = input()
print("Enter the operation")
op = input()
if op == "+":
    print(int(num1) + int(num2))
elif op == "-":
    print(int(num1) - int(num2))
elif op == "*":
    print(int(num1) * int(num2))
elif op == "/":
    print(int(num1) / int(num2))
else:
    print("Invalid operation")
    ## calculate the sum of two numbers