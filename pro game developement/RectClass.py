import pygame
pygame.init()

screen = pygame.display.set_mode([500, 500])
red = (255, 0, 0)
white = (255, 255, 255)
yellow = (255, 255, 0)
green = (0, 255, 0)
blue = (0, 0, 255)
black = (0, 0, 0)

screen.fill(white)

class rectangles():
    def __init__(self, col, pos, size, bwid=0):
        self.col = col
        self.pos = pos
        self.size = size 
        self.bwid = bwid
        self.scr = screen
    
    def draw(self):
        rect = pygame.Rect(
            self.pos[0] - self.size // 2,
            self.pos[1] - self.size // 2,
            self.size,
            self.size
        )
        pygame.draw.rect(self.scr, self.col, rect, self.bwid)
    
    def growrect(self, x):
        self.size += x
        rect = pygame.Rect(
            self.pos[0] - self.size // 2,
            self.pos[1] - self.size // 2,
            self.size,
            self.size
        )
        pygame.draw.rect(self.scr, self.col, rect, self.bwid)

position = (300, 300)
size = 156
bwidth = 2
pygame.draw.rect(screen, black, pygame.Rect(position[0]-size//2, position[1]-size//2, size, size), bwidth)
pygame.display.update()

R4 = rectangles(yellow, (250, 200), size - 40)
R3 = rectangles(red, (250, 200), size)
R2 = rectangles(blue, (250, 200), size + 40)
R1 = rectangles(green, (250, 200), size + 80)

while True:
    for event in pygame.event.get():
        if event.type == pygame.MOUSEBUTTONDOWN:
            R1.draw()
            R2.draw()
            R3.draw()
            R4.draw()
            pygame.display.update()
        
        elif event.type == pygame.MOUSEBUTTONUP:
            R1.growrect(10)
            R2.growrect(10)
            R3.growrect(10)
            R4.growrect(10)
            pygame.display.update()
        
        elif event.type == pygame.QUIT:
            pygame.quit()
            exit()