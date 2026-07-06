import pygame
import random
from settings import *
class Food:
    def __init__(self):
        self.randomize()
    def randomize(self, snake_body=None):
        while True:
            pos = [random.randint(0, (WIDTH // CELL_SIZE)-1),random.randint(0, (HEIGHT // CELL_SIZE)-1)]
            if snake_body is None or pos not in snake_body:
                self.position = pos
                break
    def draw(self, screen):
        x=self.position[0] * CELL_SIZE
        y=self.position[1] * CELL_SIZE
        pygame.draw.rect(screen,FOOD_COLOR,(x, y, CELL_SIZE, CELL_SIZE),border_radius=5)