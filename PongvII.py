# this is a game of pong
#  ## write me a game of pong
import pygame
import random
import sys
import time
from pygame.locals import *
#  ## write me a game of pong
#  ## write me a game of pong
import turtle
turtle = turtle.Turtle()
turtle.speed(0)
turtle.pensize(3)
turtle.hideturtle()
#  ## write me a game of pong
## wirte the black background
turtle.color("black")
## write the paddle
turtle.penup()
turtle.goto(-350, 0)
turtle.pendown()
turtle.goto(-350, 100)
turtle.goto(-350, -100)
turtle.penup()
turtle.goto(350, 0)
turtle.pendown()
turtle.goto(350, 100)
turtle.goto(350, -100)
turtle.penup()
turtle.goto(0, 0)
turtle.pendown()
turtle.goto(0, 300)
turtle.goto(0, -300)
turtle.penup()
turtle.goto(0, 0)
turtle.pendown()
turtle.goto(0, 300)
turtle.goto(0, -300)
turtle.penup()
turtle.goto(0, 0)
turtle.pendown()
turtle.goto(0, 300)
## write the ball
turtle.penup()
turtle.goto(0, 0)
turtle.pendown()
turtle.goto(0, 0)
turtle.goto(0, 0)
turtle.goto(0, 0)
turtle.goto(0, 0)
turtle.goto(0, 0)
turtle.goto(0, 0)
turtle.goto(0, 0)
## write the ai paddle
turtle.penup()
turtle.goto(350, 0)
turtle.pendown()
turtle.goto(350, 100)
turtle.goto(350, -100)
turtle.penup()
turtle.goto(350, 0)
turtle.pendown()
turtle.goto(350, 100)
turtle.goto(350, -100)
turtle.penup()
## write the bots ai
turtle.goto(350, 0)
turtle.pendown()
turtle.goto(350, 100)
turtle.goto(350, -100)
turtle.penup()
turtle.goto(350, 0)
turtle.pendown()
turtle.goto(350, 100)
turtle.goto(350, -100)
turtle.penup()
turtle.goto(350, 0)
turtle.pendown()
turtle.goto(350, 100)
turtle.goto(350, -100)
turtle.penup()
turtle.goto(350, 0)
turtle.pendown()
turtle.goto(350, 100)
turtle.goto(350, -100)
turtle.penup()
turtle.goto(350, 0)
turtle.pendown()
turtle.goto(350, 100)
turtle.goto(350, -100)
turtle.penup()
turtle.goto(350, 0)
turtle.pendown()
turtle.goto(350, 100)
turtle.goto(350, -100)
turtle.penup()
turtle.goto(350, 0)
turtle.pendown()
turtle.goto(350, 100)
turtle.goto(350, -100)
turtle.penup()
turtle.goto(350, 0)
turtle.pendown()
turtle.goto(350, 100)
turtle.goto(350, -100)
turtle.penup()
turtle.goto(350, 0)
turtle.pendown()
turtle.goto(350, 100)
turtle.goto(350, -100)
turtle.penup()
turtle.goto(350, 0)
turtle.pendown()
turtle.goto(350, 100)
turtle.goto(350, -100)
turtle.penup()
turtle.goto(350, 0)
turtle.pendown()
turtle.goto(350, 100)
turtle.goto(350, -100)
turtle.penup()
turtle.goto(350, 0)
turtle.pendown()
turtle.goto(350, 100)
turtle.goto(350, -100)
turtle.penup()
turtle.goto(350, 0)
turtle.pendown()
turtle.goto(350, 100)
turtle.goto(350, -100)
turtle.penup()
turtle.goto(350, 0)
turtle.pendown()
turtle.goto(350, 100)
turtle.goto(350, -100)
turtle.penup()
turtle.goto(350, 0)
turtle.pendown()
turtle.goto(350, 100)
turtle.goto(350, -100)
turtle.penup()
turtle.goto(350, 0)
turtle.pendown()
turtle.goto(350, 100)
turtle.goto(350, -100)
turtle.penup()

## stop the program from closing
turtle.mainloop()