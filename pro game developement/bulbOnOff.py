import pygame, time, sys

pygame.init()
WIDTH = 800
HEIGHT = 600
dsurface = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Bulb Switch Simulator")

bg_off = pygame.image.load("bulb_on.jpg")
bg_off = pygame.transform.scale(bg_off, (WIDTH, HEIGHT))
bg_on = pygame.image.load("bulb_off.jpg")
bg_on = pygame.transform.scale(bg_on, (WIDTH, HEIGHT))

font1 = pygame.font.SysFont("Times New Roman", 60)

def showtext(text, font, colour, pos, background, delay=2):
    dsurface.fill((255, 255, 255))
    dsurface.blit(background, (0, 0))
    render_text = font.render(text, True, colour)
    dsurface.blit(render_text, pos)
    pygame.display.update()
    time.sleep(delay)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    showtext("SWITCH: OFF", font1, (150), (260, 260), bg_off, delay=1.5)
    showtext("SWITCH: ON",  font1, (150),  (280, 260), bg_on,  delay=1.5)
