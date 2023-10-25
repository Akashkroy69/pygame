# step 1:  pip install pygame python package installer
import pygame


# 3 important parts: 1. game window, 2. game loop 3. event handler

# step 2 : initialize
pygame.init()

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 800

# SCREEN SET UP: 1. game window
screen = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))

run = True
# 2. game loop
while run:


    # event handler
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
          run = False

pygame.quit()
