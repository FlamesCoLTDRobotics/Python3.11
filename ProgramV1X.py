
import pygame 
import sys 

pygame.init() 
screen = pygame.display.set_mode((400, 300)) 
pygame.display.set_caption('Hello World GUI') 
font = pygame.font.Font(None, 32) 
text = font.render('Hello World!', True, (255, 0, 0)) 
screen.blit(text, (100, 150))   # draw text on the screen at position 100,150  
while 1:   # main loop   
    for event in pygame.event.get():   # check for any events    
        if event.type == pygame.QUIT:       # if user clicks close window     
            sys.exit()                      # close the application   

    pygame.display.update()               # update the display