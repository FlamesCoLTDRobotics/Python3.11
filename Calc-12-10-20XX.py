# Define functions for the calculator

def add(x, y):
  return x + y

def subtract(x, y):
  return x - y

def multiply(x, y):
  return x * y

def divide(x, y):
  return x / y

# Prompt the user for input

print("Enter first number:")
x = float(input())

print("Enter second number:")
y = float(input())

print("Enter operation (+, -, *, /):")
op = input()

# Compute and display the result

if op == "+":
  result = add(x, y)
elif op == "-":
  result = subtract(x, y)
elif op == "*":
  result = multiply(x, y)
elif op == "/":
  result = divide(x, y)
else:
  print("Invalid operator")

print("Result:", result)
