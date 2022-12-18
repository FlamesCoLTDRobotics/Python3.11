def calculator():
  while True:
    # Get the input from the user
    num1 = input("Enter the first number: ")
    operator = input("Enter the operator (+, -, *, /): ")
    num2 = input("Enter the second number: ")

    # Convert the input to numbers (if possible)
    try:
      num1 = float(num1)
      num2 = float(num2)
    except ValueError:
      print("Invalid input. Please try again.")
      continue

    # Perform the requested operation
    if operator == "+":
      result = num1 + num2
    elif operator == "-":
      result = num1 - num2
    elif operator == "*":
      result = num1 * num2
    elif operator == "/":
      result = num1 / num2
    else:
      print("Invalid operator. Please try again.")
      continue

    # Output the result
    print("Result:", result)

# Run the calculator
calculator()
