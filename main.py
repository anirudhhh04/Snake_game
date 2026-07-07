import pygame
import sys
from food import Food
from snake import Snake
from settings import *
from scoreboard import ScoreBoard
from game import draw_grid
pygame.init()
big_font=pygame.font.SysFont("Arial", 60, bold=True)
small_font=pygame.font.SysFont("Arial", 28)
pause_font=pygame.font.SysFont("Arial", 60, bold=True)
screen=pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Snake Game")
clock=pygame.time.Clock()
snake=Snake()
food=Food()
scoreboard=ScoreBoard()
running=True
over=False
paused=False
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_p and not over:
                paused = not paused
            if over:
                if event.key == pygame.K_r:
                    snake=Snake()
                    food=Food()
                    scoreboard.reset()
                    over=False
                    paused=False

                elif event.key == pygame.K_ESCAPE:
                    running = False

            else:

                if event.key == pygame.K_UP and snake.direction != "DOWN":
                    snake.direction = "UP"

                elif event.key == pygame.K_DOWN and snake.direction != "UP":
                    snake.direction = "DOWN"

                elif event.key == pygame.K_LEFT and snake.direction != "RIGHT":
                    snake.direction = "LEFT"

                elif event.key == pygame.K_RIGHT and snake.direction != "LEFT":
                    snake.direction = "RIGHT"
    if not over and not paused:
        grow=False
        if snake.body[0] == food.position:
            scoreboard.increase()
            food.randomize(snake.body)
            grow=True
        snake.move(grow)
        if snake.check_collision():
            over=True
    screen.fill(BACKGROUND)
    draw_grid(screen)
    food.draw(screen)
    snake.draw(screen)
    scoreboard.draw(screen)
    if over:
        game_text = big_font.render("GAME OVER", True, (255, 60, 60))
        restart_text = small_font.render("Press R to Restart", True, (255, 255, 255))
        quit_text = small_font.render("Press ESC to Quit", True, (255, 255, 255))
        screen.blit(game_text, (120, 220))
        screen.blit(restart_text, (150, 300))
        screen.blit(quit_text, (170, 340))
    if paused:
        pause_text=pause_font.render("PAUSED",True,(255, 255, 0))
        screen.blit(pause_text,(180, 250))
    pygame.display.update()
    clock.tick(FPS)
scoreboard.save()
pygame.quit()
sys.exit()