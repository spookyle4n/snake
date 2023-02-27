import pygame
import random

# Initialize Pygame
pygame.init()

# Define the game screen size
SCREEN_WIDTH = 600
SCREEN_HEIGHT = 600
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption('Snake Game')

# Define the game colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

# Define the snake's starting position and size
snake_pos = [300, 300]
snake_size = 20
snake_body = [[snake_pos[0], snake_pos[1]],
              [snake_pos[0]-snake_size, snake_pos[1]],
              [snake_pos[0]-2*snake_size, snake_pos[1]]]

# Define the food's position and size
food_pos = [random.randrange(1, (SCREEN_WIDTH//snake_size)) * snake_size,
            random.randrange(1, (SCREEN_HEIGHT//snake_size)) * snake_size]
food_size = 20

# Define the score font
font = pygame.font.SysFont(None, 50)

# Define the game clock
clock = pygame.time.Clock()

# Define the game variables
direction = 'RIGHT'
change_to = direction
score = 0

# Define the function to draw the snake and the food
def draw_snake(snake_body):
    for pos in snake_body:
        pygame.draw.rect(screen, BLUE, pygame.Rect(pos[0], pos[1], snake_size, snake_size))

def draw_food(food_pos):
    pygame.draw.rect(screen, RED, pygame.Rect(food_pos[0], food_pos[1], food_size, food_size))

# Define the game over function
def game_over():
    screen.fill(BLACK)
    message = font.render("Game over! Your score is " + str(score), True, WHITE)
    message_rect = message.get_rect()
    message_rect.center = (SCREEN_WIDTH//2, SCREEN_HEIGHT//2)
    screen.blit(message, message_rect)
    pygame.display.flip()
    pygame.time.wait(3000)
    pygame.quit()
    quit()

# Run the game loop
while True:
    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                change_to = 'RIGHT'
            elif event.key == pygame.K_LEFT:
                change_to = 'LEFT'
            elif event.key == pygame.K_UP:
                change_to = 'UP'
            elif event.key == pygame.K_DOWN:
                change_to = 'DOWN'

    # Update the snake's direction
    if change_to == 'RIGHT' and direction != 'LEFT':
        direction = 'RIGHT'
    elif change_to == 'LEFT' and direction != 'RIGHT':
        direction = 'LEFT'
    elif change_to == 'UP' and direction != 'DOWN':
        direction = 'UP'
    elif change_to == 'DOWN' and direction != 'UP':
        direction = 'DOWN'

    # Move the snake
    if direction == 'RIGHT':
        snake_pos[0] += snake_size
    elif direction == 'LEFT':
        snake_pos[0] -= snake_size
    elif direction == 'UP':
        snake_pos[1] -= snake_size
    elif direction == 'DOWN':
        snake_pos[1] += snake_size

    # Check for game over
   
