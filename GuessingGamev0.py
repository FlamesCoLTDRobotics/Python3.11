print("Welcome to Guessing Game 1.0a [C] - Flames Co. LTD")
print("Guess a number between 1 and 10")
guess = int(input("Enter your guess: "))
## make a algrothim to guess the number
## use a random number generator
import random
randomnum = random.randint(1,10)
if guess == randomnum:
    print("You guessed correctly")
else:
    print("You guessed incorrectly")
    print("The correct answer was", randomnum)
    print("Better luck next time")