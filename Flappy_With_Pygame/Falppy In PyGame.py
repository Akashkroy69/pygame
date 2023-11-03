# imports
import pygame
import math
from pygame import mixer 

# The line from pygame.locals import * is often used in Pygame scripts to import a set of constants
#  and symbolic names that represent various keycodes, event types, and other constants used in Pygame. 
# It's a convenient way to make these constants 
# accessible without prefixing them with pygame. every time you use them.
from pygame.locals import *

# initialization
pygame.init()
# screen setup
SCREEN_HEIGHT = 810
SCREEN_WIDTH = 830
screen = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))
pygame.display.set_caption("Flappy In PyGame")

# sound
# Starting the mixer 
mixer.init() 
# Loading the song 
mixer.music.load(r"Codingal\PYGAME\Flappy_With_Pygame\helsound.mp3") 
# Setting the volume 
mixer.music.set_volume(0.3) 
# Start playing the song 
mixer.music.play() 


# load image
background = pygame.image.load(r'Codingal\PYGAME\Flappy_With_Pygame\flapbg.png')
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
        self.groundStartsAt = 650
        self.SPACE_clicked = False
        self.soundEffectFactorHelicopter = 0

        for birdNum in range(1,4): 
            img = pygame.image.load(fr"Codingal\PYGAME\Flappy_With_Pygame\hel{birdNum}.png")
            img = pygame.transform.scale(img,(50,50))
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
            self.gravity += 1
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

        # replays helicopter sound effect
        self.soundEffectFactorHelicopter += 1
        if self.soundEffectFactorHelicopter == 2000:
            self.soundEffectFactorHelicopter = 0
            mixer.music.play()

            # bird fly logic
        if pygame.key.get_pressed()[K_SPACE] and self.rect.y>0 and self.SPACE_clicked == False:
            # self.SPACE_clicked = True
            self.rect.y -= 20
            # self.image = pygame.transform.rotate(self.images[self.index],90)

        # bird rotation
        self.image = pygame.transform.rotate(self.images[self.index],self.gravity*-2)

            
        


# 2 using sprite to make a goup of images, here group of bird images.
#  this creates a list in which we can add our images
bird_group = pygame.sprite.Group()
flappyBird = Bird(100, int(SCREEN_HEIGHT/2))
bird_group.add(flappyBird)


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
    screen.blit(ground,(ground_scroll,700))
    ground_scroll -= scroll_speed

    # 3 drawing the object from bird group
    bird_group.draw(screen)
    bird_group.update()

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
