import pygame
import turtle
print("Welcome to Turtle!")

## write a tkinter 800x800
screen = turtle.Screen()
screen.title("Turtle")
screen.bgcolor("black")
screen.setup(width=800, height=800)
screen.tracer(0,0)
screen.bgcolor("white")
screen.update()

# disable the maximize button
turtle.buttonmode(False)