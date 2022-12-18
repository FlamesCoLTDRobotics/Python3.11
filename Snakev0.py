
import turtle
import pygame

#Set up the window
wn = turtle.Screen()
wn.bgcolor("black")
wn.title("Snake")
wn.setup(width=600, height=600)
wn.tracer(0)

#Snake head
head = turtle.Turtle()
head.speed(0)
head.shape("square")
head.color("green")
head.penup()
head.goto(0, 0)
head.direction = "stop"

#Game loop
while True:
    wn.update()

    #Movement
    if head.direction == "up":
        y = head.ycor()
        head.sety(y + 20)

    if head.direction == "down":
        y = head.ycor()
        head.sety(y - 20)

    if head.direction == "left":
        x = head.xcor()
        head.setx(x - 20)

    if head.direction == "right":
        x = head.xcor()
        head.setx(x + 20)

    #Check for keyboard input
    def move_up():
        head.direction = "up"
    def move_down():
        head.direction = "down"
    def move_left():
        head.direction = "left"
    def move_right():
        head.direction = "right"

    wn.listen()
    wn.onkeypress(move_up, "Up")
    wn.onkeypress(move_down, "Down")
    wn.onkeypress(move_left, "Left")
    wn.onkeypress(move_right, "Right")

wn.mainloop()
 