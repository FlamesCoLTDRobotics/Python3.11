# define the main function
def main():
  # get the user's input
  num1 = float(input("Enter the first number: "))
  num2 = float(input("Enter the second number: "))
  operator = input("Enter an operator (+, -, *, /): ")

  # perform the calculation
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
    return

  # print the result
  print(f"{num1} {operator} {num2} = {result}")

# run the main function
if __name__ == "__main__":
  main()
