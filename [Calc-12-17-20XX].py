def calculate():
  # Get the user's input
  num1 = float(input("Enter the first number: "))
  operator = input("Enter the operator (+, -, *, /): ")
  num2 = float(input("Enter the second number: "))

  # Perform the calculation
  if operator == "+":
    result = num1 + num2
  elif operator == "-":
    result = num1 - num2
  elif operator == "*":
    result = num1 * num2
  elif operator == "/":
    result = num1 / num2
  else:
    result = "Invalid operator"

  # Print the result
  print(result)

# Run the calculator
calculate()
