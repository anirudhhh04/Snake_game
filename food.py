import pygame
import random
from settings import *
class Food:
    def __init__(self):
        self.image=pygame.image.load("assets/images/apple.png").convert_alpha()
        self.image=pygame.transform.scale(self.image,(FOOD_SIZE,FOOD_SIZE))
        self.randomize()
    def randomize(self, snake_body=None):
        while True:
            pos = [random.randint(0, (WIDTH // CELL_SIZE) - 1),random.randint(0, (HEIGHT // CELL_SIZE) - 1)]
            if snake_body is None or pos not in snake_body:
                self.position=pos
                break
    def draw(self, screen):
        x=self.position[0]*CELL_SIZE
        y=self.position[1]*CELL_SIZE
        offset=(FOOD_SIZE-CELL_SIZE)//2
        screen.blit(self.image, (x-offset, y-offset))
        