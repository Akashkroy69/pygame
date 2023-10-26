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
player = pygame.Rect((350,350,50,50))

run = True
# 2. game loop
while run:
#   in each loop the following code will fill the canvas with fresh color so
# previous trail will be covered.
  screen.fill((0,0,0))

#  drawing the player object
  pygame.draw.rect(screen,(117,66,247),player)

#  control
  key = pygame.key.get_pressed()
  if key[pygame.K_UP]:
    player.y -= 1
  elif key[pygame.K_DOWN]:
    player.y += 1
  elif key[pygame.K_LEFT]:
    player.x -= 1
  elif key[pygame.K_RIGHT]:
    player.x += 1


    # step 3: event handler
  for event in pygame.event.get():
    # logic for closing the window
    if event.type == pygame.QUIT:
        run = False
#we need to update the screen in each loop so player object that we are creating here becomes visble
# else as in each loop canvas  
  pygame.display.update()

pygame.quit()
