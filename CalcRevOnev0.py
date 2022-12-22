
def calculator():
  # Ask the user to enter two numbers
  num1 = float(input("Enter first number: "))
  num2 = float(input("Enter second number: "))

  # Ask the user to enter an operator
  print("Enter an operator (+, -, *, /): ")
  operator = input()

  # Calculate the result
  if operator == "+":
    result = num1 + num2
  elif operator == "-":
    result = num1 - num2
  elif operator == "*":
    result = num1 * num2
  elif operator == "/":
    result = num1 / num2
  else:
    print("Invalid operator")

  # Print the result
  print("The result is:", result)

# Call the calculator function
calculator()
print("Thanks for using this calculator, goodbye.")
