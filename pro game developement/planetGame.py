import pygame

pygame.init()
WIDTH = 700
HEIGHT = 700
screen = pygame.display.set_mode((WIDTH, HEIGHT))
screen.fill((255,255,255))
pygame.display.update()
earth_img = pygame.image.load("earth.png")
mars_img = pygame.image.load("mars.png")
saturn_img = pygame.image.load("saturn.png")
earth = pygame.transform.scale(earth_img, (70,70))
mars = pygame.transform.scale(mars_img, (70,70))
saturn = pygame.transform.scale(saturn_img, (90,90))
screen.blit(earth, (150, 100))
screen.blit(mars, (150, 200))
screen.blit(saturn, (150, 300))
font = pygame.font.SysFont("Comic Sans", 40)
txt1 = font.render("Rings", True, (0,0,0))
txt2 = font.render("Life", True, (0,0,0))
txt3 = font.render("Red Planet", True, (0,0,0))
screen.blit(txt1, (350, 100))
screen.blit(txt2, (350, 200))
screen.blit(txt3, (350, 300))
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