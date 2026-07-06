import pygame
from settings import *
class Snake:
    def __init__(self):
        self.body = [ [5, 5], [4, 5], [3, 5]]
        self.direction = "RIGHT"
    def move(self, grow=False):
            head = self.body[0].copy()
            if self.direction == "UP":
                head[1] -= 1
            elif self.direction == "DOWN":
                head[1] += 1
            elif self.direction == "LEFT":
                head[0] -= 1
            elif self.direction == "RIGHT":
                head[0] += 1
            # Screen wrapping
            head[0]%=WIDTH // CELL_SIZE
            head[1]%=HEIGHT // CELL_SIZE
            self.body.insert(0, head)
            if not grow:
                self.body.pop()

    def draw(self, screen):
        for block in self.body:
            x = block[0] * CELL_SIZE
            y = block[1] * CELL_SIZE
            pygame.draw.rect(screen,SNAKE_COLOR,(x, y, CELL_SIZE, CELL_SIZE),border_radius=4)
    def check_collision(self): #for checking head collision
        head=self.body[0]
        return head in self.body[1:]