import pygame
import sys
import math

# Initialize Pygame
pygame.init()

# Constants
WIDTH, HEIGHT = 800, 600
PLAYER_SIZE = 50
PLAYER_COLOR = (0, 0, 255)
ENEMY_SIZE = 30
ENEMY_COLOR = (255, 0, 0)
BULLET_SIZE = 10
BULLET_COLOR = (0, 255, 0)
PLAYER_SPEED = 5
BULLET_SPEED = 10
ENEMY_SPEED = 3
ENEMY_SPAWN_INTERVAL = 60

# Create the game window
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Top-Down Shooter")

# Player variables
player_x = WIDTH // 2
player_y = HEIGHT // 2
player_angle = 0

# Bullet variables
bullets = []

# Enemy variables
enemies = []
enemy_spawn_counter = 0

# Main game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Handle player movement
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        player_x -= PLAYER_SPEED
    if keys[pygame.K_RIGHT]:
        player_x += PLAYER_SPEED
    if keys[pygame.K_UP]:
        player_y -= PLAYER_SPEED
    if keys[pygame.K_DOWN]:
        player_y += PLAYER_SPEED

    # Player shooting
    if keys[pygame.K_SPACE]:
        bullet_x = player_x + PLAYER_SIZE // 2 - BULLET_SIZE // 2
        bullet_y = player_y + PLAYER_SIZE // 2 - BULLET_SIZE // 2
        bullet_angle = player_angle
        bullets.append((bullet_x, bullet_y, bullet_angle))

    # Enemy spawning
    if enemy_spawn_counter >= ENEMY_SPAWN_INTERVAL:
        enemy_x = 0
        enemy_y = 0
        enemy_angle = math.atan2(player_y - enemy_y, player_x - enemy_x)
        enemies.append((enemy_x, enemy_y, enemy_angle))
        enemy_spawn_counter = 0
    else:
        enemy_spawn_counter += 1

    # Move bullets
    bullets = [(bx + BULLET_SPEED * math.cos(ba), by + BULLET_SPEED * math.sin(ba), ba) for bx, by, ba in bullets]

    # Move enemies
    enemies = [(ex + ENEMY_SPEED * math.cos(ea), ey + ENEMY_SPEED * math.sin(ea), ea) for ex, ey, ea in enemies]

    # Remove out-of-bounds bullets
    bullets = [(bx, by, ba) for bx, by, ba in bullets if 0 <= bx < WIDTH and 0 <= by < HEIGHT]

    # Remove out-of-bounds enemies
    enemies = [(ex, ey, ea) for ex, ey, ea in enemies if 0 <= ex < WIDTH and 0 <= ey < HEIGHT]

    # Check for collisions
    for bullet in bullets:
        for enemy in enemies:
            bx, by, _ = bullet
            ex, ey, _ = enemy
            distance = math.hypot(bx - ex, by - ey)
            if distance < BULLET_SIZE + ENEMY_SIZE:
                bullets.remove(bullet)
                enemies.remove(enemy)

    # Draw everything
    screen.fill((0, 0, 0))
    for bullet in bullets:
        bx, by, _ = bullet
        pygame.draw.rect(screen, BULLET_COLOR, (bx, by, BULLET_SIZE, BULLET_SIZE))
    for enemy in enemies:
        ex, ey, _ = enemy
        pygame.draw.rect(screen, ENEMY_COLOR, (ex, ey, ENEMY_SIZE, ENEMY_SIZE))
    pygame.draw.rect(screen, PLAYER_COLOR, (player_x, player_y, PLAYER_SIZE, PLAYER_SIZE))

    pygame.display.update()

pygame.quit()
sys.exit()
