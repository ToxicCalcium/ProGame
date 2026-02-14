import pygame

pygame.init()
WIDTH = 700
HEIGHT = 700
screen = pygame.display.set_mode((WIDTH, HEIGHT))
screen.fill((255,255,255))
pygame.display.update()
candyCrush = pygame.image.load("CandyCrush.jpg")
ludo = pygame.image.load("Ludo.png")
subwaySurfer = pygame.image.load("SubwaySurfer.png")
templeRun = pygame.image.load("TempleRun.png")
screen.blit(candyCrush, (150, 100))
screen.blit(ludo, (150, 200))
screen.blit(subwaySurfer, (150, 300))
screen.blit(templeRun, (150, 400))
font = pygame.font.SysFont("Comic Sans", 40)
txt1 = font.render("Ludo", True, (0,0,0))
txt2 = font.render("Temple Run", True, (0,0,0))
txt3 = font.render("Candy Crush", True, (0,0,0))
txt4 = font.render("Subway Surfers", True, (0,0,0))
screen.blit(txt1, (350, 100))
screen.blit(txt2, (350, 200))
screen.blit(txt3, (350, 300))
screen.blit(txt4, (350, 400))
pygame.display.update()
running = True

while running:
    event = pygame.event.poll()
    if event.type == pygame.QUIT:
        running = False
    elif event.type == pygame.MOUSEBUTTONDOWN:
        pos = pygame.mouse.get_pos()
        pygame.draw.circle(screen, (0,0,0), (pos), 20, 0)
        pygame.display.update()
    elif event.type == pygame.MOUSEBUTTONUP:
        pos2 = pygame.mouse.get_pos()
        pygame.draw.line(screen, (0,0,0), (pos), (pos2), 5)
        pygame.draw.circle(screen, (0,0,0), (pos2), 20, 0)
        pygame.display.update()