import pygame

pygame.font.init()
WIDTH = 900
HEIGHT = 700
pygame.display.set_caption("Space Fighters")
dsurface = pygame.display.set_mode((WIDTH, HEIGHT))
White = (255,255,255)
Black = (0,0,0)
Red = (255,0,0)
Yellow = (255,255,0)
Split = pygame.Rect(WIDTH//2 - 5, 0, 10, HEIGHT)
HealthFont = pygame.font.SysFont("Times New Roman", 40)
WinFont = pygame.font.SysFont("Times New Roman", 100)
ShipVelocity = 5
BulletVelocity = 7
MaxBullets = 3
ShipWidth = 55
ShipHeight = 40
FPS = 60
#Yellow Ship on the left facing right (90), Red Ship on the right facing left (270) 
YellowShip_img = pygame.image.load("YellowShip.jpg")
YellowShip = pygame.transform.rotate(pygame.transform.scale(YellowShip_img, (ShipWidth, ShipHeight)), 90)
RedShip_img = pygame.image.load("RedShip.jpg")
RedShip = pygame.transform.rotate(pygame.transform.scale(RedShip_img, (ShipWidth, ShipHeight)), 270)
Spacebg_img = pygame.image.load("SpaceGamebg.jpg")
Spacebg = pygame.transform.scale(Spacebg_img, (WIDTH, HEIGHT))

def draw_window(red, yellow, red_bullets, yellow_bullets, red_hp, yellow_hp):
    dsurface.blit(Spacebg, (0,0))
    pygame.draw.rect(dsurface, White, Split)
    red_health_text = HealthFont.render("Health: " + str(red_hp), 1, Red)
    yellow_health_text = HealthFont.render("Health: " + str(yellow_hp), 1, Yellow)
    dsurface.blit(red_health_text, (15,15))
    dsurface.blit(yellow_health_text, ((WIDTH - 15), 15))
    dsurface.blit(RedShip, (red.x, red.y))
    dsurface.blit(YellowShip, (yellow.x, yellow.y))
    for bullet in red_bullets:
        pygame.draw.rect(dsurface, Red, bullet)
    for bullet in yellow_bullets:
        pygame.draw.rect(dsurface, Yellow, bullet)
    pygame.display.update()

def red_movement(keys_pressed, red):
    if keys_pressed[pygame.K_a] and red.x - ShipVelocity > 0:
        red.x -= ShipVelocity
    if keys_pressed[pygame.K_d] and red.x + ShipVelocity + red.width < Split.x:
        red.x += ShipVelocity
    if keys_pressed[pygame.K_w] and red.y - ShipVelocity > 0:
        red.y -= ShipVelocity
    if keys_pressed[pygame.K_s] and red.y + ShipVelocity + red.height < HEIGHT - 15:
        red.y += ShipVelocity