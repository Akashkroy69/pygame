import pygame

lastP = pygame.time.get_ticks()
print(lastP)
while True:

   timeNow = pygame.time.get_ticks()
#    print(timeNow)
   if timeNow - lastP > 1500:      
      print(timeNow,lastP)



# print(timeNow)