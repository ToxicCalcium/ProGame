import pygame, time

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

def draw_window(red, yellow, red_bullets, yellow_bullets, red_health, yellow_health):
    dsurface.blit(Spacebg, (0,0))
    pygame.draw.rect(dsurface, White, Split)
    red_health_text = HealthFont.render("Health: " + str(red_health), 1, Red)
    yellow_health_text = HealthFont.render("Health: " + str(yellow_health), 1, Yellow)
    dsurface.blit(red_health_text, (720,15))
    dsurface.blit(yellow_health_text, (15, 15))
    dsurface.blit(RedShip, (red.x, red.y))
    dsurface.blit(YellowShip, (yellow.x, yellow.y))
    for bullet in red_bullets:
        pygame.draw.rect(dsurface, Red, bullet)
    for bullet in yellow_bullets:
        pygame.draw.rect(dsurface, Yellow, bullet)
    pygame.display.update()

def red_movement(keys_pressed, red):
    if keys_pressed[pygame.K_a] and red.x - ShipVelocity > Split.x:
        red.x -= ShipVelocity
    if keys_pressed[pygame.K_d] and red.x + ShipVelocity + red.width < WIDTH:
        red.x += ShipVelocity
    if keys_pressed[pygame.K_w] and red.y - ShipVelocity > 0:
        red.y -= ShipVelocity
    if keys_pressed[pygame.K_s] and red.y + ShipVelocity + red.height < HEIGHT - 15:
        red.y += ShipVelocity

def yellow_movement(keys_pressed, yellow):
    if keys_pressed[pygame.K_LEFT] and yellow.x - ShipVelocity > 0:
        yellow.x -= ShipVelocity
    if keys_pressed[pygame.K_RIGHT] and yellow.x + ShipVelocity + yellow.width < Split.x:
        yellow.x += ShipVelocity
    if keys_pressed[pygame.K_UP] and yellow.y - ShipVelocity > 0:
        yellow.y -= ShipVelocity
    if keys_pressed[pygame.K_DOWN] and yellow.y + ShipVelocity + yellow.height < HEIGHT - 15:
        yellow.y += ShipVelocity

def bullet_move(yellow_bullets, red_bullets, red, yellow):
    for bullet in yellow_bullets:
        bullet.x += BulletVelocity
        if red.colliderect(bullet):
            pygame.event.post(pygame.event.Event(RedHit))
            yellow_bullets.remove(bullet)

        elif bullet.x < 0:
            yellow_bullets.remove(bullet)

    for bullet in red_bullets:
        bullet.x -= BulletVelocity
        if yellow.colliderect(bullet):
            pygame.event.post(pygame.event.Event(YellowHit))
            red_bullets.remove(bullet)
        
        elif bullet.x > WIDTH:
            red_bullets.remove(bullet)

def win_display(text):
    drawtext = WinFont.render(text, 1, White)
    dsurface.blit(drawtext, (WIDTH/2 - drawtext.get_width()/2, HEIGHT/2 - drawtext.get_height()/2))
    pygame.display.update()
    pygame.time.delay(5000)

def main():
    red = pygame.Rect(700, HEIGHT/2, ShipWidth, ShipHeight)
    yellow = pygame.Rect(100, HEIGHT/2, ShipWidth, ShipHeight)
    bullets = []
    yellow_bullets = []
    red_bullets = []
    red_health = 10
    yellow_health = 10
    clock = pygame.time.Clock()
    run = True
    while run:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                pygame.quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE and len(yellow_bullets) < MaxBullets:
                    bullet = pygame.Rect(yellow.x + yellow.width, yellow.y + yellow.height//2-2, 10, 5)
                    yellow_bullets.append(bullet)
                if event.key == pygame.K_LCTRL and len(red_bullets) < MaxBullets:
                    bullet = pygame.Rect(red.x, red.y + red.height//2-2, 10, 5)
                    red_bullets.append(bullet)
            if event.type == RedHit:
                red_health = red_health - 1
            if event.type == YellowHit:
                yellow_health = yellow_health - 1
        win_text = ""
        if red_health <=0:
            win_text = "yellow win"
        if yellow_health <=0:
            win_text = "red win"
        if win_text != "":
            win_display(win_text)
            break
        keys_pressed = pygame.key.get_pressed()
        yellow_movement(keys_pressed, yellow)
        red_movement(keys_pressed, red)
        bullet_move(yellow_bullets, red_bullets, red, yellow)
        draw_window(red, yellow, red_bullets, yellow_bullets, red_health, yellow_health)
    main()

if __name__ == "__main__":
    main()