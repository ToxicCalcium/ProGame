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