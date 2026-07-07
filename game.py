import pygame
from settings import *

def draw_grid(screen):
    for x in range(0, WIDTH, CELL_SIZE):
        pygame.draw.line(screen,GRID_COLOR,(x, 0),(x, HEIGHT))

    for y in range(0, HEIGHT, CELL_SIZE):
        pygame.draw.line(screen,GRID_COLOR,(0, y),(WIDTH, y))