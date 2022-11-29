import pygame
import turtle
 
# Set up the screen
wn = turtle.Screen()
wn.title("Frogger")
wn.bgcolor("black")
wn.setup(width=600, height=600)
wn.tracer(0) # Turns off the screen updates 
 
# Create a player turtle (frog)
player = turtle.Turtle()  # Creates a new turtle object from the Turtle class in the turtle module 
player.speed(0) # Sets animation speed to 0 (fastest possible speed)  
player.shape("square") # Sets shape of the player to a square 
player.color("green") # Sets color of player to green  								   	    # Moves player up 5 pixels on y axis every time it is called  

def move_up():     # Defines function for moving up  

    y = player.ycor()     # Gets current y coordinate of frog and stores it in variable y     

    y += 5        # Increases value of y by 5 each time function is called      

    player.sety(y)      # Sets new value of y as current position for frog      

 
# Keyboard bindings for movement directions  

wn.listen()            # Tells program to listen for keyboard input   

wn.onkeypress(move_up, "Up")     # When Up arrow key is pressed call move_up function     

while True:           # While loop that runs forever until break statement is reached      

     wn.update()        # Updates screen with changes made