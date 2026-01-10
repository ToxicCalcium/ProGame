import pygame, random
pygame.init()

WIDTH = 700
HEIGHT = 900
screen = pygame.display.set_mode((WIDTH, HEIGHT))
score = 0
gameover = False

class circleobjects():
    def __init__(self, col, pos, rad, bwid = 0):
        self.col = col
        self.pos = pos
        self.rad = rad
        self.bwid = bwid
        self.scr = screen
    
    