import turtle
import tkinter
import pygame

# Create the window
window = tkinter.Tk()
window.title("Shooter")
window.geometry("400x400")
window.configure(background='black')

# Create the canvas
canvas = tkinter.Canvas(window, width=400, height=400)
canvas.pack()

# Create a turtle
t = turtle.RawTurtle(canvas)
t.speed(0)
t.shape('square')
t.color('white')
t.shapesize(stretch_wid=0.7, stretch_len=1.1)

# Create a bullet
bullet = turtle.RawTurtle(canvas)
bullet.speed(0)
bullet.shape('triangle')
bullet.color('blue')
bullet.shapesize(stretch_wid=0.3, stretch_len=0.5)
bullet.penup()

# Create the pygame window
pygame.init()
pygame.display.set_caption("Shooter")
screen = pygame.display.set_mode((400, 400))

# Create a list of enemies
enemies = []

# Initialize the game
done = False

# Main game loop
while not done:
    # Process user input
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

    # Update the game state
    t.forward(2)
    pygame.display.flip()

# Close the window
pygame.quit()
window.destroy()
