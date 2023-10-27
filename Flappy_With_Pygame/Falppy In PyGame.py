# imports
import pygame
from pygame.locals import *

#  initialization
pygame.init()


# screen setup
SCREEN_HEIGHT = 500
SCREEN_WIDTH = 800
screen = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))
pygame.display.set_caption("Flappy In PyGame")

# main game loop
runningStatus = True
while runningStatus:

    # for closing the window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            runningStatus = False



# closing the window
pygame.quit()
