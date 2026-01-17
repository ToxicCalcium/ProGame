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
YellowHit = pygame.USEREVENT + 1
RedHit = pygame.USEREVENT + 2
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

def yellow_movement(keys_pressed, yellow):
    if keys_pressed[pygame.K_LEFT] and yellow.x - ShipVelocity > Split.width:
        yellow.x -= ShipVelocity
    if keys_pressed[pygame.K_RIGHT] and yellow.x + ShipVelocity + yellow.width < WIDTH:
        yellow.x += ShipVelocity
    if keys_pressed[pygame.K_UP] and yellow.y - ShipVelocity > 0:
        yellow.y -= ShipVelocity
    if keys_pressed[pygame.K_DOWN] and yellow.y + ShipVelocity + yellow.height < HEIGHT - 15:
        yellow.y += ShipVelocity

def bullet_move(yellow_bullets, red_bullets, red, yellow):
    for bullet in yellow_bullets:
        bullet.x -= BulletVelocity
        if red.colliderect(bullet):
            pygame.event.post(pygame.event.Event(RedHit))
            yellow_bullets.remove(bullet)

        elif bullet.x < 0:
            yellow_bullets.remove(bullet)

    for bullet in red_bullets:
        bullet.x += BulletVelocity
        if yellow.colliderect(bullet):
            pygame.event.post(pygame.event.Event(YellowHit))
            red_bullets.remove(bullet)
        
        elif bullet.x > WIDTH:
            red_bullets.remove(bullet)

def win_display(text):
    drawtext = WinFont.render(text, 1, White)
    dsurface.blit(drawtext, (WIDTH/2 - drawtext.get_width/2, HEIGHT/2 - drawtext.get_height/2))
    pygame.display.update()
    pygame.time.delay(5000)