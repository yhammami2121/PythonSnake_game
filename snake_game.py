# Snake Game
# Author: Youssef Hammami
# GitHub: https://github.com/yhammami2121
# Description: This is a classic Snake game implemented in Python using the Pygame library.
# Date: 06/16/2023

# The code in this file is owned and developed by Youssef Hammami.
# You are free to modify and distribute this code for personal and educational purposes.
# If you wish to use this code for commercial purposes, please contact Youssef Hammami for permission.

# Import required libraries
import pygame
import random

# Initialize Pygame
pygame.init()

# Game window dimensions
WIDTH = 800
HEIGHT = 600

# Define colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)

# Snake and apple dimensions
BLOCK_SIZE = 20
SNAKE_SPEED = 10

# Create the game window
win = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Snake Game")

# Initialize the clock
clock = pygame.time.Clock()

# Define fonts
font_large = pygame.font.Font(None, 40)
font_medium = pygame.font.Font(None, 30)
font_small = pygame.font.Font(None, 24)

# Helper function to display text on the screen
def draw_text(text, font, color, x, y):
    """
    Draw text on the game screen.

    Parameters:
    - text: The text string to display.
    - font: The font object for the text.
    - color: The color of the text.
    - x: The x-coordinate of the text position.
    - y: The y-coordinate of the text position.
    """
    text_surface = font.render(text, True, color)
    text_rect = text_surface.get_rect()
    text_rect.center = (x, y)
    win.blit(text_surface, text_rect)

# Snake game function
def game_loop():
    """
    Main game loop for the Snake game.
    """
    game_over = False
    game_quit = False

    # Initial snake position and direction
    x1 = WIDTH / 2
    y1 = HEIGHT / 2
    x1_change = 0
    y1_change = 0

    # Snake body
    snake_body = []
    snake_length = 1

    # Generate the first apple
    apple_x = round(random.randrange(0, WIDTH - BLOCK_SIZE) / BLOCK_SIZE) * BLOCK_SIZE
    apple_y = round(random.randrange(0, HEIGHT - BLOCK_SIZE) / BLOCK_SIZE) * BLOCK_SIZE

    # Score variable
    score = 0

    while not game_quit:
        
        while game_over:
            win.fill(BLACK)
            draw_text("Game Over! Press Q-Quit or C-Play Again", font_large, RED, WIDTH / 2, HEIGHT / 2)
            pygame.display.update()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    game_quit = True
                    game_over = False
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        game_quit = True
                        game_over = False
                    elif event.key == pygame.K_c:
                        game_loop()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_quit = True
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT and x1_change != BLOCK_SIZE:
                    x1_change = -BLOCK_SIZE
                    y1_change = 0
                elif event.key == pygame.K_RIGHT and x1_change != -BLOCK_SIZE:
                    x1_change = BLOCK_SIZE
                    y1_change = 0
                elif event.key == pygame.K_UP and y1_change != BLOCK_SIZE:
                    x1_change = 0
                    y1_change = -BLOCK_SIZE
                elif event.key == pygame.K_DOWN and y1_change != -BLOCK_SIZE:
                    x1_change = 0
                    y1_change = BLOCK_SIZE

        if x1 >= WIDTH or x1 < 0 or y1 >= HEIGHT or y1 < 0:
            game_over = True

        x1 += x1_change
        y1 += y1_change
        win.fill(BLACK)
        pygame.draw.rect(win, GREEN, [apple_x, apple_y, BLOCK_SIZE, BLOCK_SIZE])
        snake_head = [x1, y1]
        snake_body.append(snake_head)
        
        draw_text("Score: " + str(score), font_small, RED, WIDTH / 2, 20)

        if len(snake_body) > snake_length:
            del snake_body[0]

        for segment in snake_body[:-1]:
            if segment == snake_head:
                game_over = True

        for segment in snake_body:
            pygame.draw.rect(win, WHITE, [segment[0], segment[1], BLOCK_SIZE, BLOCK_SIZE])

        pygame.display.update()

        if x1 == apple_x and y1 == apple_y:
            apple_x = round(random.randrange(0, WIDTH - BLOCK_SIZE) / BLOCK_SIZE) * BLOCK_SIZE
            apple_y = round(random.randrange(0, HEIGHT - BLOCK_SIZE) / BLOCK_SIZE) * BLOCK_SIZE
            snake_length += 1
            score += 10

        clock.tick(SNAKE_SPEED)

    pygame.quit()


# Run the game
game_loop()
