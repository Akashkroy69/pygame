# step 1:  pip install pygame python package installer
import pygame


# 3 important parts: 1. game window, 2. game loop 3. event handler

# step 2 : initialize
pygame.init()

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 800

# SCREEN SET UP: 1. game window
screen = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))

# player step 4
player = pygame.Rect((0,0,50,50))

run = True
# 2. game loop
while run:
#  drawing the player object
 pygame.draw.rect(screen,(117,66,247),player)

    # step 3: event handler
 for event in pygame.event.get():
    # logic for closing the window
    if event.type == pygame.QUIT:
        run = False

pygame.quit()
