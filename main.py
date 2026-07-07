import pygame
import sys
from food import Food
from snake import Snake
from settings import *
from scoreboard import ScoreBoard
from game import draw_grid
pygame.init()
title_font=pygame.font.SysFont("Arial", 72, bold=True)
menu_font=pygame.font.SysFont("Arial", 32)
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
game_state="MENU"
paused=False
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if game_state == "MENU":
                if event.key == pygame.K_RETURN:
                    game_state = "PLAYING"
                elif event.key == pygame.K_ESCAPE:
                    running = False
                continue
            if event.key == pygame.K_p and game_state=="PLAYING":
                paused = not paused
            if game_state=="GAME_OVER":
                if event.key == pygame.K_r:
                    snake=Snake()
                    food=Food()
                    food.randomize(snake.body)
                    scoreboard.reset()
                    paused=False
                    game_state="PLAYING"

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
    if game_state=="PLAYING" and not paused:
        grow=False
        if snake.body[0] == food.position:
            scoreboard.increase()
            food.randomize(snake.body)
            grow=True
        snake.move(grow)
        if snake.check_collision():
            game_state="GAME_OVER"
    screen.fill(BACKGROUND)
    draw_grid(screen)
    if game_state=="MENU":
        title=title_font.render("SNAKE GAME",True,(0, 255, 0))
        play=menu_font.render("Press ENTER to Play",True,(255, 255, 255))
        exit_text=menu_font.render("Press ESC to Exit",True,(255, 255, 255))
        screen.blit(title, (70, 130))
        screen.blit(play, (150, 280))
        screen.blit(exit_text, (165, 340))
        pygame.display.update()
        clock.tick(FPS)
        continue
    food.draw(screen)
    snake.draw(screen)
    scoreboard.draw(screen)
    if game_state=="GAME_OVER":
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