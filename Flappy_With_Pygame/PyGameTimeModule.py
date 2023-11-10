import pygame
# The pygame.time.Clock class is used to control the frame rate of your game. 
# It provides a way to track time and limit the frame rate, 
# ensuring that your game runs at a consistent speed across different systems.
clock = pygame.time.Clock()

# -----------------------------------------------------
# The tick method of the Clock class is used to control the frame rate. It should be called once per frame, 
# and you pass the desired frames per second (fps) as an argument. 
# This method returns the time elapsed since the last call to tick.
clock.tick(60)  # Limits the frame rate to 60 frames per second
# This is often used in the game loop to control how fast the loop iterates, 
# preventing the game from running too fast or too slow.

# -------------------------------------------------------
# The get_ticks function returns the number of milliseconds since the Pygame module was initialized. 
# It's commonly used to measure elapsed time or to create timers.
current_time = pygame.time.get_ticks()
# This is often used to measure the time between events, for animations, or to create delays.

# ---------------------------------------------------------
# The delay function pauses the program's execution for a specified number of milliseconds. 
# It can be used to create delays or control the pace of certain events.
pygame.time.delay(1000)  # Delays the program for 1000 milliseconds (1 second)
# This function is useful for creating timed events, such as delays between game states or animations.


# ---------------------------------------------------------
pygame.time.wait(1000)