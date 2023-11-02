import pygame
pygame.init()

# Screen dimensions
screen_width, screen_height = 400, 400
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Sprite Example")

# Colors
white = (255, 255, 255)

# Create a sprite
sprite_width, sprite_height = 50, 50
sprite_x, sprite_y = screen_width // 2, screen_height // 2
sprite = pygame.Rect(sprite_x, sprite_y, sprite_width, sprite_height)

# Set the initial speed
sprite_speed = 1

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        sprite.x -= sprite_speed
    if keys[pygame.K_RIGHT]:
        sprite.x += sprite_speed
    if keys[pygame.K_UP]:
        sprite.y -= sprite_speed
    if keys[pygame.K_DOWN]:
        sprite.y += sprite_speed

    screen.fill(white)
    pygame.draw.rect(screen, (0, 0, 255), sprite)
    pygame.display.flip()

pygame.quit()
