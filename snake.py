import pygame
from settings import *
class Snake:
    def __init__(self):
        self.body = [ [5, 5], [4, 5], [3, 5]]
        self.direction = "RIGHT"
        self.head_image = pygame.image.load("assets/images/SNAKEE.png").convert_alpha()
        self.head_image = pygame.transform.smoothscale(self.head_image,(HEAD_SIZE,HEAD_SIZE))
        self.head_down=self.head_image
        #initializing all rotated images
        self.head_right=pygame.transform.rotate(self.head_image,90)
        self.head_up=pygame.transform.rotate(self.head_image, 180)
        self.head_left=pygame.transform.rotate(self.head_image,-90)
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
            head[1]%=GAME_HEIGHT // CELL_SIZE
            self.body.insert(0, head)
            if not grow:
                self.body.pop()

    def draw(self, screen):
        for i, block in enumerate(self.body):
            x = block[0]*CELL_SIZE
            y = HUD_HEIGHT+block[1]*CELL_SIZE
            if i==0:                         # Draw Head
                if self.direction == "UP":
                    head = self.head_up
                elif self.direction == "RIGHT":
                    head = self.head_right
                elif self.direction == "DOWN":
                    head = self.head_down
                elif self.direction == "LEFT":
                    head = self.head_left
                offset=(HEAD_SIZE-CELL_SIZE)//2
                screen.blit(head,(x - offset, y - offset))
            #Draw Body
            else:
                pygame.draw.rect(screen,SNAKE_COLOR,(x,y, CELL_SIZE, CELL_SIZE),border_radius=6)
    def check_collision(self): #for checking head collision
        head=self.body[0]
        return head in self.body[1:]