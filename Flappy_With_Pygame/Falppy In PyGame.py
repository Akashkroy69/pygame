# imports
import pygame
from pygame.locals import *

#  initialization
pygame.init()
# screen setup
SCREEN_HEIGHT = 200
SCREEN_WIDTH = 300
screen = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))
pygame.display.set_caption("Flappy In PyGame")


# load image
background = pygame.image.load(r'Codingal\PYGAME\Flappy_With_Pygame\flapbg.png')


# main game loop
runningStatus = True
while runningStatus:
    screen.blit(background,(0,0))

    # for closing the window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            runningStatus = False
    pygame.display.update()


# closing the window
pygame.quit()
