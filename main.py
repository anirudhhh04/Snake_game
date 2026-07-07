import pygame
import sys
from food import Food
from snake import Snake
from settings import *
from scoreboard import ScoreBoard
from game import draw_grid
pygame.init()
selected=0
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
                if event.key == pygame.K_UP:
                    selected=(selected-1)%2
                elif event.key == pygame.K_DOWN:
                    selected=(selected+1)%2
                elif event.key==pygame.K_RETURN:
                    if selected==0:
                        game_state="PLAYING"
                    elif selected==1:
                        running=False
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
    pygame.draw.rect(screen,(30, 30, 30),(0, 0, WIDTH, HUD_HEIGHT))
    pygame.draw.line(screen,(0, 255, 0),(0, HUD_HEIGHT),(WIDTH, HUD_HEIGHT),2)
    draw_grid(screen)
    if game_state == "MENU":
        panel = pygame.Rect(80, 60, 440, 470)
        pygame.draw.rect(screen,(35,35,35),panel,border_radius=18)
        pygame.draw.rect(screen,(0,220,0),panel,width=3,border_radius=18)
        logo = pygame.transform.smoothscale(snake.head_up,(80,80))
        screen.blit(logo,(260,75))
        title = title_font.render("SNAKE GAME",True,(0,255,0))
        screen.blit(title,title.get_rect(center=(WIDTH//2,180)))
        high = menu_font.render(f"High Score : {scoreboard.high_score}",True,(255,255,0))
        screen.blit(high,high.get_rect(center=(WIDTH//2,240)))
        # ---------- START BUTTON ----------
        start_rect = pygame.Rect(170,300,260,55)
        color = (0,160,0) if selected==0 else (55,55,55)
        pygame.draw.rect(screen,color,start_rect,border_radius=12)
        pygame.draw.rect(screen,(255,255,255),start_rect,width=2,border_radius=12)

        start = menu_font.render("START GAME",True,(255,255,255))
        screen.blit(start,start.get_rect(center=start_rect.center))
        # ---------- EXIT BUTTON ----------

        exit_rect = pygame.Rect(170,380,260,55)
        color = (200,40,40) if selected==1 else (55,55,55)
        pygame.draw.rect(screen,color,exit_rect,border_radius=12)
        pygame.draw.rect(screen,(255,255,255),exit_rect,width=2,border_radius=12)
        exit_text = menu_font.render("EXIT",True,(255,255,255))
        screen.blit(exit_text,exit_text.get_rect(center=exit_rect.center))
        
        help_text = small_font.render("↑ ↓ Select      ENTER Confirm",True,(180,180,180))
        screen.blit(help_text,help_text.get_rect(center=(WIDTH//2,490)))
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