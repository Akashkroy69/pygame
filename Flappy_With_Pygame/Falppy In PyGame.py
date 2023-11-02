# imports
import pygame
import math
# The line from pygame.locals import * is often used in Pygame scripts to import a set of constants
#  and symbolic names that represent various keycodes, event types, and other constants used in Pygame. 
# It's a convenient way to make these constants 
# accessible without prefixing them with pygame. every time you use them.
from pygame.locals import *

# initialization
pygame.init()
# screen setup
SCREEN_HEIGHT = 200
SCREEN_WIDTH = 280
screen = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))
pygame.display.set_caption("Flappy In PyGame")


# load image
background = pygame.image.load(r'Codingal\PYGAME\Flappy_With_Pygame\flapbg.png')
ground = pygame.image.load(r'Codingal\PYGAME\Flappy_With_Pygame\ground.png')

# setting the frame rate
clock = pygame.time.Clock()
fps = 60
# game variables 
ground_scroll = 0
scroll_speed = 3

runningStatus = True



# main game loop
while runningStatus:

    # setting up the frame rate
    clock.tick(fps)

    # to render the image for background
    screen.blit(background,(0,0))
    # to render image for ground
    screen.blit(ground,(ground_scroll,158))
    ground_scroll -= scroll_speed

    # code for continuous scroll effect
    if abs(ground_scroll) > 40:
        ground_scroll = 0


    # for closing the window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            runningStatus = False
    pygame.display.update()


# closing the window
pygame.quit()
