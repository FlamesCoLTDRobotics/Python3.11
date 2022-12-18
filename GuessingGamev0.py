
import random

#generate a random number
number = random.randint(1,10)

#ask user to guess the number
print("Guess the number between 1 and 10")

#keep track of number of guesses
guess_count = 0

#infinite loop
while True:
    #get the guess from user
    guess = int(input())

    #increment the guess count
    guess_count = guess_count + 1

    #check if the guess is correct
    if guess == number:
        print("Correct!")
        print("You guessed it in " + str(guess_count) + " guesses.")
        break
    #check if the guess is too high
    elif guess > number:
        print("Incorrect! Your guess is too high.")
    #otherwise, the guess is too low
    else:
        print("Incorrect! Your guess is too low.")
