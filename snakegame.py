import pygame
import time
import random

pygame.init()

# Set up display
width = 640
height = 480
display = pygame.display.set_mode((width, height))
pygame.display.set_caption('Snake Game')

# Colors
white = (255, 255, 255)
black = (0, 0, 0)
red = (255, 0, 0)
green = (0, 255, 0)

# Snake and food
snake_pos = [100, 50]
snake_body = [[100, 50], [90, 50], [80, 50]]
food_pos = [random.randrange(1, (width//10)) * 10, random.randrange(1, (height//10)) * 10]
food_spawn = True

# Direction
direction = 'RIGHT'
change_to = direction

# Initial Speed
speed = 15

# Score
score = 0

# Game Over
game_over = False

# Main Function
def gameLoop():
    global change_to
    global direction
    global snake_pos
    global food_pos
    global food_spawn
    global score
    global game_over
    global speed
    
    while not game_over:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    change_to = 'UP'
                if event.key == pygame.K_DOWN:
                    change_to = 'DOWN'
                if event.key == pygame.K_LEFT:
                    change_to = 'LEFT'
                if event.key == pygame.K_RIGHT:
                    change_to = 'RIGHT'
        
        # Change direction
        if change_to == 'UP' and direction != 'DOWN':
            direction = 'UP'
        if change_to == 'DOWN' and direction != 'UP':
            direction = 'DOWN'
        if change_to == 'LEFT' and direction != 'RIGHT':
            direction = 'LEFT'
        if change_to == 'RIGHT' and direction != 'LEFT':
            direction = 'RIGHT'
        
        # Moving the snake
        if direction == 'UP':
            snake_pos[1] -= 10
        if direction == 'DOWN':
            snake_pos[1] += 10
        if direction == 'LEFT':
            snake_pos[0] -= 10
        if direction == 'RIGHT':
            snake_pos[0] += 10
        
        # Snake body growing mechanism
        snake_body.insert(0, list(snake_pos))
        if snake_pos[0] == food_pos[0] and snake_pos[1] == food_pos[1]:
            score += 10
            food_spawn = False
        else:
            snake_body.pop()
        
        if not food_spawn:
            food_pos = [random.randrange(1, (width//10)) * 10, random.randrange(1, (height//10)) * 10]
        food_spawn = True
        
        display.fill(black)
        for pos in snake_body:
            pygame.draw.rect(display, green, pygame.Rect(pos[0], pos[1], 10, 10))
        
        pygame.draw.rect(display, white, pygame.Rect(food_pos[0], food_pos[1], 10, 10))
        
        # Game Over conditions
        if snake_pos[0] < 0 or snake_pos[0] > width-10 or snake_pos[1] < 0 or snake_pos[1] > height-10:
            game_over = True
        for block in snake_body[1:]:
            if snake_pos[0] == block[0] and snake_pos[1] == block[1]:
                game_over = True
        
        pygame.display.update()
        speed += 1
        time.sleep(10/speed)
    
    pygame.quit()
    quit()

# Call the gameLoop function
gameLoop()
