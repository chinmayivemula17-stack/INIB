import pygame
import random

# Start pygame
pygame.init()

# Create window
screen = pygame.display.set_mode((600, 400))

# Window title
pygame.display.set_caption("Snake Game")

# Clock
clock = pygame.time.Clock()

# Font
font = pygame.font.SysFont(None, 35)

# Colors
BLACK = (0, 0, 0)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
WHITE = (255, 255, 255)

# Snake settings
snake_size = 20
snake_x = 100
snake_y = 100

# Snake movement
x_change = 0
y_change = 0

# Snake body
snake_body = []
snake_length = 1

# Food position
food_x = random.randint(0, 580)
food_y = random.randint(0, 380)

# Score
score = 0

# Game states
running = True
game_over = False

# Game loop
while running:

    # Background
    screen.fill(BLACK)

    # Events
    for event in pygame.event.get():

        # Close window
        if event.type == pygame.QUIT:
            running = False

        # Keyboard controls
        if event.type == pygame.KEYDOWN:

            if event.key == pygame.K_LEFT:
                x_change = -20
                y_change = 0

            if event.key == pygame.K_RIGHT:
                x_change = 20
                y_change = 0

            if event.key == pygame.K_UP:
                y_change = -20
                x_change = 0

            if event.key == pygame.K_DOWN:
                y_change = 20
                x_change = 0

    # Move snake
    snake_x += x_change
    snake_y += y_change

    # Border collision
    if snake_x < 0 or snake_x >= 600 or snake_y < 0 or snake_y >= 400:
        game_over = True
        running = False

    # Draw food
    pygame.draw.rect(screen,
                     RED,
                     (food_x, food_y, 20, 20))

    # Snake head
    snake_head = []
    snake_head.append(snake_x)
    snake_head.append(snake_y)

    # Add head to snake body
    snake_body.append(snake_head)

    # Remove extra body parts
    if len(snake_body) > snake_length:
        del snake_body[0]

    # Self collision
    for block in snake_body[:-1]:

        if block == snake_head:
            game_over = True
            running = False

    # Draw snake
    for i, block in enumerate(snake_body):

        x = block[0]
        y = block[1]

        # Snake head
        if i == len(snake_body) - 1:

            # Curved head
            pygame.draw.rect(screen,
                             GREEN,
                             (x, y, snake_size, snake_size),
                             border_radius=8)

            # Left eye
            pygame.draw.circle(screen,
                               BLACK,
                               (x + 6, y + 6),
                               2)

            # Right eye
            pygame.draw.circle(screen,
                               BLACK,
                               (x + 14, y + 6),
                               2)

        # Snake body
        else:

            pygame.draw.rect(screen,
                             GREEN,
                             (x, y,
                              snake_size, snake_size))

    # Food collision
    if abs(snake_x - food_x) < 20 and abs(snake_y - food_y) < 20:

        # New food position
        food_x = random.randint(0, 580)
        food_y = random.randint(0, 380)

        # Increase score
        score += 1

        # Increase snake length
        snake_length += 1

    # Score text
    score_text = font.render("Score: " + str(score),
                             True,
                             WHITE)

    screen.blit(score_text, (10, 10))

    # Update screen
    pygame.display.update()

    # Game speed
    clock.tick(6)

# Game Over screen
if game_over:

    screen.fill(BLACK)

    game_over_text = font.render("GAME OVER!",
                                 True,
                                 RED)

    final_score = font.render("Final Score: " + str(score),
                              True,
                              WHITE)

    screen.blit(game_over_text, (200, 150))
    screen.blit(final_score, (190, 200))

    pygame.display.update()

    # Wait 3 seconds
    pygame.time.delay(3000)

# Quit game
pygame.quit()
