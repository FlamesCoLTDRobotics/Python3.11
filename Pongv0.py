import pygame, sys, random, time
from pygame.locals import *
pygame.init()
clock = pygame.time.Clock()
pygame.display.set_caption('Pong')
screen = pygame.display.set_mode((640, 480))

  # Main Game Loop:

while True:

        for event in pygame.event.get():

            if event.type == QUIT:

                sys.exit()

        screen.fill((0, 0, 0)) # Clears the screen and fills it with black (RGB)

        clock.tick(60) # Limits the game to 60 frames per second (FPS)

        pygame.display.update() # Updates the screen

        ## wrie your code here
        ## display a turtle for paddle one and two
        ## draw the ai paddle
        import turtle as t
        t.speed(0)
        t.color("white")
        t.penup()
        ## draw it on the right
        t.goto(300, 0)
        t.pendown()
        t.goto(300, 100)
        t.goto(300, 0)
        t.goto(300, -100)
        t.penup()
        ## draw it on the left
        ## draw a red one on the left
        t.color("red")
        t.goto(-300, 0)
        t.pendown()
        t.goto(-300, 100)
        t.goto(-300, 0)
        t.goto(-300, -100)
        t.penup()
        ## draw the ball
        t.color("white")
        t.goto(0, 0)
        t.pendown()
        t.circle(10)
        t.penup()
        ## draw the score
        ## make the ai fo the game
        ## make the ball move
        ## make the ball bounce off the walls
        ## make the ball bounce off the paddles
        ## make the ball reset when it goes off the screen
        def ball_reset():
            t.goto(0, 0)
            t.setheading(random.randint(0, 360))
        def ball_move():
            t.forward(10)
            if t.xcor() > 300:
                ball_reset()
            if t.xcor() < -300:
                ball_reset()
            if t.ycor() > 240:
                t.setheading(360 - t.heading())
            if t.ycor() < -240:
                t.setheading(360 - t.heading())
       