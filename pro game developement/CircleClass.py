import pygame
pygame.init()

screen = pygame.display.set_mode([500, 500])
red = (255,0,0)
white = (255,255,255)
yellow = (255,255,0)
green = (0,255,0)
blue = (0,0,255)
black = (0,0,0)

screen.fill(white)

class circles():
    def __init__(self, col, pos, rad, bwid=0):
        self.col = col
        self.pos = pos
        self.rad = rad
        self.bwid = bwid
        self.scr = screen
    
    def draw(self):
        pygame.draw.circle(self.scr, self.col, self.pos, self.rad, self.bwid) #if bwid is 0, the circle is filled but if it is >0 then it is outlined
    
    def growcircle(self, x):
        self.rad += x
        pygame.draw.circle(self.scr, self.col, self.pos, self.rad, self.bwid)

position = (300, 300)
radius = 78
bwidth = 2
pygame.draw.circle(screen, black, position, radius, bwidth)
pygame.display.update()

C4 = circles(yellow, (250, 200), radius-20)
C3 = circles(red, (250,200), radius)
C2 = circles(blue, (250,200), radius+20)
C1 = circles(green, (250,200), radius+40)

while (1):
    for event in pygame.event.get():
        if event.type == pygame.MOUSEBUTTONDOWN:
            C1.draw()
            C2.draw()
            C3.draw()
            C4.draw()
            pygame.display.update()
        
        elif event.type == pygame.MOUSEBUTTONUP:
            C1.growcircle(5)
            C2.growcircle(5)
            C3.growcircle(5)
            C4.growcircle(5)
            pygame.display.update()
        
        elif event.type == pygame.QUIT:
            pygame.quit()