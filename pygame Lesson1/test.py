# 1. screen 2. game loop/main loop 3. event handler
# step 1 : import
import pygame

# initialize the pygame module
pygame.init()

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

# Screen setup
screen = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))
pygame.display.set_caption("Introduction")

#player 
player = pygame.Rect((100,100,50,50))

image = pygame.image.load('img.png')



runningStatus = True
# game loop/ main
while runningStatus:
 # to draw the object
  pygame.draw.rect(screen,"red",player)


  
  key = pygame.key.get_pressed()
  if key[pygame.K_UP]:
    player.y += 1
# Event handler
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      runningStatus = False
# we always have to update the scree so after creating different ements object get displayed in correct order
  pygame.display.update()

# closing the window/game
pygame.quit()


