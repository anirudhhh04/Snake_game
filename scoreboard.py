import pygame
from settings import *
class ScoreBoard:
    def __init__(self):
        self.score=0
        self.font = pygame.font.SysFont("Arial", 28)
        try:
            with open("highscore.txt","r") as file:
                self.high_score = int(file.read())
        except:
            self.high_score = 0
    def increase(self):
        self.score+=1
        if self.score > self.high_score:
            self.high_score = self.score

    def draw(self, screen):
        score = self.font.render(f"Score: {self.score}",True,TEXT_COLOR)
        high = self.font.render(f"High Score: {self.high_score}",True,TEXT_COLOR)
        screen.blit(score, (10, 10))
        screen.blit(high, (WIDTH-200, 10))

    def save(self):
        with open("highscore.txt", "w") as file:
            file.write(str(self.high_score))

    def reset(self):
        self.score = 0