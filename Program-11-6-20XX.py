## write a caclulator

#!/usr/bin/env python3

# Program 11.6: Calculator.py
# Calculates the sum, difference, product, and quotient of two numbers

def main():
    print("This program calculates the sum, difference, product, and quotient of two numbers.")
    print()

    # Get the first number and store it in a variable
    num1 = float(input("Enter the first number: "))

    # Get the second number and store it in a variable
    num2 = float(input("Enter the second number: "))

    # Calculate the sum,
    sum = num1 + num2
    print("The sum of", num1, "and", num2, "is", sum)
    print()

    # Calculate the difference
    difference = num1 - num2
    print("The difference of", num1, "and", num2, "is", difference)
    print()

    # Calculate the product
    product = num1 * num2
    print("The product of", num1, "and", num2, "is", product)
    print()

    # Calculate the quotient
    quotient = num1 / num2
    print("The quotient of", num1, "and", num2, "is", quotient)
    print()

# Call the main function
main()

# /Users/blitz/Library/Mobile Documents/com~apple~CloudDocs/:Coding/~Swift/Program-11-6-20XX.
