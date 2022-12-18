
import pygame
import random

# Initialize game engine
pygame.init()

# Window
SIZE = (800, 600)
TITLE = "Donkey Kong"
screen = pygame.display.set_mode(SIZE)
pygame.display.set_caption(TITLE)

# Timer
clock = pygame.time.Clock()
refresh_rate = 60

# Colors
RED = (255, 0, 0)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
YELLOW = (255, 255, 0)

# Game loop
done = False

while not done:
    # Event processing (React to key presses, mouse clicks, etc.)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True     

    # Game logic (Check for collisions, update points, etc.)
    ''' leave this section alone for now '''

    # Drawing code (Describe the picture. It isn't actually drawn yet.)
    screen.fill(BLACK)
    pygame.draw.rect(screen, RED, [400, 300, 50, 50])
    pygame.draw.rect(screen, YELLOW, [200, 200, 50, 50])
    pygame.draw.rect(screen, WHITE, [100, 100, 50, 50])

    # Update screen (Actually draw the picture in the window.)
    pygame.display.flip()


    # Limit refresh rate of game loop 
    clock.tick(refresh_rate)

# Close window and quit
pygame.quit()