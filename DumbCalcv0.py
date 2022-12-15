def add(x, y):
  return x + y

def subtract(x, y):
  return x - y

def multiply(x, y):
  return x * y

def divide(x, y):
  if y == 0:
    return "Cannot divide by 0!"
  return x / y

def calculator():
  while True:
    num1 = float(input("Enter the first number: "))
    num2 = float(input("Enter the second number: "))
    operation = input("Enter the operation (+, -, *, /): ")

    if operation == "+":
      result = add(num1, num2)
    elif operation == "-":
      result = subtract(num1, num2)
    elif operation == "*":
      result = multiply(num1, num2)
    elif operation == "/":
      result = divide(num1, num2)
    else:
      result = "Invalid operation!"

    print(result)
    repeat = input("Do you want to perform another operation? (y/n) ")
    if repeat.lower() != "y":
      break

calculator()
