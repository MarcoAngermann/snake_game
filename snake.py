import pygame
import time
import random

pygame.init()

display_color = (0, 0, 0)
snake_color = (139, 69, 19)
food_color = (200, 200, 200)

width, height = 800, 600
display = pygame.display.set_mode((width, height))
pygame.display.set_caption("Snake Game")

snake_block = 10
snake_speed = 15

font_style = pygame.font.SysFont(None, 35)
score_font = pygame.font.SysFont(None, 25)

def show_score(score):
    value = score_font.render(f"Punkte: {score}", True, (255, 255, 255))
    display.blit(value, [0, 0])

def draw_snake(block_size, snake_list):
    for block in snake_list:
        pygame.draw.rect(display, snake_color, [block[0], block[1], block_size, block_size])

def message(msg, color):
    text = font_style.render(msg, True, color)
    display.blit(text, [width / 6, height / 3])

def game_loop():
    game_over = False
    game_close = False

    x, y = width / 2, height / 2
    x_change, y_change = snake_block, 0 

    snake_list = [[x - i * snake_block, y] for i in range(4)]
    length_of_snake = 4


    food_x = round(random.randrange(0, width - snake_block) / 10.0) * 10.0
    food_y = round(random.randrange(0, height - snake_block) / 10.0) * 10.0

    while not game_over:

        while game_close:
            display.fill(display_color)
            message("You Loose! Q = Quit Game, R = Restart Game", (255, 255, 255))
            show_score(length_of_snake - 1)
            pygame.display.update()

            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        game_over = True
                        game_close = False
                    if event.key == pygame.K_r:
                        game_loop()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    x_change = -snake_block
                    y_change = 0
                elif event.key == pygame.K_RIGHT:
                    x_change = snake_block
                    y_change = 0
                elif event.key == pygame.K_UP:
                    y_change = -snake_block
                    x_change = 0
                elif event.key == pygame.K_DOWN:
                    y_change = snake_block
                    x_change = 0

        if x >= width or x < 0 or y >= height or y < 0:
            game_close = True

        x += x_change
        y += y_change
        display.fill(display_color)
        pygame.draw.rect(display, food_color, [food_x, food_y, snake_block, snake_block])
        
        snake_head = [x, y]
        snake_list.append(snake_head)
        if len(snake_list) > length_of_snake:
            del snake_list[0]

        for block in snake_list[:-1]:
            if block == snake_head:
                game_close = True

        draw_snake(snake_block, snake_list)
        show_score(length_of_snake - 1)

        pygame.display.update()

        if x == food_x and y == food_y:
            food_x = round(random.randrange(0, width - snake_block) / 10.0) * 10.0
            food_y = round(random.randrange(0, height - snake_block) / 10.0) * 10.0
            length_of_snake += 1

        time.sleep(1 / snake_speed)

    pygame.quit()
    quit()

game_loop()