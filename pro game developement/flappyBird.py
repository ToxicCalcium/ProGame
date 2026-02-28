import pygame, random

pygame.init()
WIDTH = 400
HEIGHT = 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()

class bird:
    def __init__(self):
        self.x = 80
        self.y = 300
        self.vel = 0
    
    def jump(self):
        self.vel = -10

    def birdmove(self):
        self.vel += 0.5
        self.y += self.vel

    def draw(self):
        pygame.draw.circle(screen, (255, 255, 0), (self.x, int(self.y)), 15)

class pipe:
    def __init__(self):
        self.x = 400
        self.height = random.randint(115, 400)
    
    def move(self):
        self.x -= 4