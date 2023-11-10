# imports
import pygame
import math
import random
# The line from pygame.locals import * is often used in Pygame scripts to import a set of constants
#  and symbolic names that represent various keycodes, event types, and other constants used in Pygame. 
# It's a convenient way to make these constants 
# accessible without prefixing them with pygame. every time you use them.
from pygame.locals import *

# initialization
pygame.init()
# screen setup
SCREEN_HEIGHT = 800
SCREEN_WIDTH = 830
screen = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))
pygame.display.set_caption("Flappy In PyGame")


# load image
background = pygame.image.load(r'Codingal\PYGAME\Flappy_With_Pygame\ev1.jpg')
background1 = pygame.transform.flip(background,False,True)
# background = pygame.transform.rotate(background,180)
ground = pygame.image.load(r'Codingal\PYGAME\Flappy_With_Pygame\ground.png')

# 1 adding a bird using sprite
class Bird(pygame.sprite.Sprite):
    def __init__(self,x,y):
        # Sprite class has already functions that will updat, draw,load,render the images.
        # we don't need to call load or blit function externally
        pygame.sprite.Sprite.__init__(self)
        # useful variables for the bird
        self.images= []
        self.index = 0
        self.counter = 0
        self.gravity = 0
        self.groundStartsAt = 658
        self.SPACE_clicked = False



        for birdNum in range(1,4): 
            img = pygame.image.load(fr"Codingal\PYGAME\Flappy_With_Pygame\bird{birdNum}.png")
            self.images.append(img)
        # this will create a reactable around the image, it's mandatory as the bird image 
        # might be of unusual shape
        self.image = self.images[self.index]
        self.rect = self.image.get_rect()
        self.rect.center = [x,y]

    # To hadnle the animation overriding 
    def update(self):
        # bird fall logic
        if self.gravity < 3:
            self.gravity += 0.5
        if self.rect.y < self.groundStartsAt:
           self.rect.y += self.gravity

        # handles the animation
        self.counter += 1
        flapGapFactor = 10

        if self.counter>=flapGapFactor:
          self.counter = 0
          self.index += 1
          if self.index>=len(self.images):
              self.index = 0
        self.image = self.images[self.index]

        # bird fly logic
        if pygame.key.get_pressed()[K_SPACE] and self.rect.y>10 and self.SPACE_clicked == False:
            # print(f"{pygame.key.get_pressed()[K_SPACE]} and {self.rect.y>=100} and {self.SPACE_clicked == False:}")
            self.SPACE_clicked = True
            self.gravity -= 2
            self.rect.y -= 5
            print(f"y: {self.rect.y}, gravity: {self.gravity}")
            # self.image = pygame.transform.rotate(self.images[self.index],90)
        # if self.SPACE_clicked == True:
        #     self.SPACE_clicked = False

        # bird rotation
        self.image = pygame.transform.rotate(self.images[self.index],self.gravity*-2)

# pipe class 
class Pipe(pygame.sprite.Sprite):
    #,fromTop: +1: from top, -1: from bottom
    def __init__(self,x,y,fromTop):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(r"Codingal\PYGAME\Flappy_With_Pygame\tower.png")
        self.rect = self.image.get_rect()
        self.pipeGap = random.randint(100,600)
        if fromTop == 1:
            self.image = pygame.transform.flip(self.image,flip_x=False,flip_y=True)
            self.rect.bottomleft = [x,y-int(self.pipeGap/2)]
        if fromTop == -1:
            # self.image = pygame.transform.flip(self.image,flip_x=False,flip_y=False)
            self.rect.topleft = [x,y + int(self.pipeGap/2)]
    def update(self):
        self.rect.x -= 4
# 2 using sprite to make a goup of images, here group of bird images.
#  this creates a list in which we can add our images
bird_group = pygame.sprite.Group()
flappyBird = Bird(100, int(SCREEN_HEIGHT/2))
bird_group.add(flappyBird)

# sprtite for pipes
pipe_group = pygame.sprite.Group()
bottomPipe = Pipe(300, int(SCREEN_HEIGHT/2) ,-1)
topPipe = Pipe(300,int(SCREEN_HEIGHT/2),1)
pipe_group.add(bottomPipe)
pipe_group.add(topPipe)

# setting the frame rate
clock = pygame.time.Clock()
fps = 60

# game variables 
ground_scroll = 0
scroll_speed = 3
runningStatus = True
pipeFrequency = 1500
lastPipe = pygame.time.get_ticks()
pipeGeneratingFactor = 0
# main game loop
while runningStatus:
    screen.fill("skyblue")
    pipeGeneratingFactor +=1
    # setting up the frame rate
    clock.tick(fps)
  
    # to render the image for background:LAYER 1
    # screen.blit(background1,(0,-300))
    screen.blit(background,(0,-200))

    # pipe draw and update
    pipe_group.draw(screen)
    pipe_group.update()

    # drawing the object from bird group: LAYER 2
    bird_group.draw(screen)
    # calling the overridden function update that will bring the movent to the bird
    bird_group.update()


    # to render image for ground: LAYER 3
    screen.blit(ground,(ground_scroll,690))
    ground_scroll -= scroll_speed

    # code for continuous scroll effect
    if runningStatus == True:
         timeNow = pygame.time.get_ticks()
        #  print(timeNow)
         if timeNow - lastPipe > pipeFrequency:
             bottomPipe = Pipe(SCREEN_WIDTH, int(SCREEN_HEIGHT/2) ,-1)
             topPipe = Pipe(SCREEN_WIDTH,int(SCREEN_HEIGHT/2),1)
             pipe_group.add(bottomPipe)
             pipe_group.add(topPipe)
             lastPipe = timeNow

         if abs(ground_scroll) > 40:
            ground_scroll = 0


    # for closing the window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            runningStatus = False
    pygame.display.update()


# closing the window
pygame.quit()
