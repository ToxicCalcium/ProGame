import pygame, time, sys

pygame.init()
WIDTH = 800
HEIGHT = 600
dsurface = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Halloween Card")
background = pygame.image.load("halloweenbg.jpg")
background = pygame.transform.scale(background, (WIDTH, HEIGHT))

font1 = pygame.font.SysFont("Times New Roman", 60)

def showtext(text, font, colour, pos, delay = 2):
    dsurface.fill((255,255,255))
    dsurface.blit(background, (0,0))
    render_text = font.render(text, True, colour)
    dsurface.blit(render_text, pos)
    pygame.display.update()
    time.sleep(delay)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    
    showtext("Happy", font1, (255, 140, 0), (300,300))
    showtext("Halloween", font1, (255, 140, 0), (400,300))