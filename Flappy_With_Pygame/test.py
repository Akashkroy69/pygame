import pygame
pygame.init()
lastP = pygame.time.get_ticks()
print(lastP)
while True:
   pygame.time.Clock().tick(1)
   # OR, pygame.time.wait(1000)
   timeNow = pygame.time.get_ticks()
   print("TIME NOW :------",timeNow)
   if timeNow - lastP > 1500:      
      print(timeNow,lastP)
      lastP = timeNow




# print(timeNow)