 ## write me a game of guessing game
if __name__ == "__main__":
    import random
    print("Hello World")
    print("I am thinking")
    print("of a number")
    print("That is randomly generated")
    print("It is computetr generated number")
    print("please guess the number")
    print("Guess it plz")
    try :
        number = int(input("Enter your guess: "))
    except ValueError:
        print("Please enter a number")
        number = int(input("Enter your guess: "))
    print("You entered: ", number)
    print("I am thinking")
    print("of a number")
    print("That is randomly generated")
    print("It is computetr generated number")
    if number == random.randint(1, 100):
        print("You guessed it!")
    else:
        print("You did not guess it!")
        print("The number was: ", random.randint(1, 100))