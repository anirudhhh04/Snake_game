import pygame
import sys
from snake import Snake
from settings import *
pygame.init()
screen=pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Snake Game")
clock=pygame.time.Clock()
snake=Snake()
running=True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                snake.direction = "UP"
            elif event.key == pygame.K_DOWN:
                snake.direction = "DOWN"
            elif event.key == pygame.K_LEFT:
                snake.direction = "LEFT"
            elif event.key == pygame.K_RIGHT:
                snake.direction = "RIGHT"
    snake.move()
    screen.fill(BACKGROUND)
    snake.draw(screen)
    pygame.display.update()
    clock.tick(FPS)
pygame.quit()
sys.exit()