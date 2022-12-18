import pygame
import turtle

# Initialize the game
pygame.init()

# Set up the window
window = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Pong")

# Create the game objects
player1 = turtle.Turtle()
player2 = turtle.Turtle()
ball = turtle.Turtle()

# Set up the game objects
player1.speed(0)
player1.shape("square")
player1.color("white")
player1.shapesize(stretch_wid=5, stretch_len=1)
player1.penup()
player1.goto(-350, 0)

player2.speed(0)
player2.shape("square")
player2.color("white")
player2.shapesize(stretch_wid=5, stretch_len=1)
player2.penup()
player2.goto(350, 0)

ball.speed(0)
ball.shape("circle")
ball.color("white")
ball.penup()
ball.goto(0, 0)

# Set up the game variables
player1_score = 0
player2_score = 0

# Disable maximize
pygame.display.set_mode((800, 600), pygame.NOFRAME)

# Generative loop
while True:
    window.fill((0, 0, 0))

    # Move the players
    player1.sety(player1.ycor() + 2)
    player2.sety(player2.ycor() - 2)

    # Move the ball
    ball.setx(ball.xcor() + 2)
    ball.sety(ball.ycor() + 2)

    # Check for a collision with the border
    if ball.ycor() > 290:
        ball.sety(290)
    if ball.ycor() < -290:
        ball.sety(-290)
    if ball.xcor() > 390:
        ball.goto(0, 0)
        player1_score += 1
    if ball.xcor() < -390:
        ball.goto(0, 0)
        player2_score += 1

    # Check for a collision with the paddles
    if (ball.xcor() > 340 and ball.xcor() < 350) and (ball.ycor() < player2.ycor() + 40 and ball.ycor() > player2.ycor() - 40):
        ball.setx(340)
    if (ball.xcor() < -340 and ball.xcor() > -350) and (ball.ycor() < player1.ycor() + 40 and ball.ycor() > player1.ycor() - 40):
        ball.setx(-340)

    # Display the scores
    window.write("Player 1: {}  Player 2: {}".format(player1_score, player2_score), align="center", font=("Courier", 24, "normal"))

    # Update the window
    pygame.display.update()