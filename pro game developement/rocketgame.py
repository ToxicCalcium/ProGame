import pygame, random

pygame.init()
WIDTH = 600
HEIGHT = 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
fuel = 5000
pygame.display.set_caption("Rocket Game")

class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("rocket.png").convert_alpha()
        self.image = pygame.transform.scale(self.image, (70,100))
        self.rect = self.image.get_rect() #creates hitbox for collision, movement detection and other events
    
    def update(self, pressed_keys):
        global fuel
        if pressed_keys[pygame.K_UP]:
            self.rect.move_ip(0, -5) #moves 0 pixels horizontally and 5 pixels up vertically (move.ip means move in place)
            fuel = fuel - 1
        
        if pressed_keys[pygame.K_DOWN]:
            self.rect.move_ip(0, 5)
            fuel = fuel - 1
        
        if pressed_keys[pygame.K_LEFT]:
            self.rect.move_ip(-5, 0)
            fuel = fuel - 1
        
        if pressed_keys[pygame.K_RIGHT]:
            self.rect.move_ip(5, 0)
            fuel = fuel - 1
        
        #Setting screen boundary for player
        if self.rect.left < 0:
            self.rect.left = 0
        
        elif self.rect.right > WIDTH:
            self.rect.right = WIDTH
        
        elif self.rect.top <= 0:
            self.rect.top = 0
        
        elif self.rect.bottom >= HEIGHT:
            self.rect.bottom = HEIGHT

class  Asteroid(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("asteroid.png").convert_alpha()
        self.image = pygame.transform.scale(self.image, (70, 70))
        self.rect = self.image.get_rect()
        self.rect.x = random.randint(50, 550)
        self.rect.y = 0
        self.speed = random.randint(1, 3)
    
    def update(self):
        self.rect.y += self.speed
        if self.rect.top >= HEIGHT:
            self.rect.x = random.randint(50, 550)
            self.rect.y = 0
            self.speed = random.randint(1, 8)


sprites = pygame.sprite.Group()
font = pygame.font.SysFont("Comic Sans", 40)
def startGame():
    player = Player()
    asteroid_group = pygame.sprite.Group()
    #asteroid = Asteroid()
    for i in range(3):
        asteroid = Asteroid()
        asteroid_group.add(asteroid)
    sprites.add(player)
    sprites.add(asteroid_group)
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()

        asteroid_group.update()
        pressed_keys = pygame.key.get_pressed()
        player.update(pressed_keys)
        Spacebg_img = pygame.image.load("SpaceGamebg.jpg")
        Spacebg = pygame.transform.scale(Spacebg_img, (WIDTH, HEIGHT))
        screen.blit(Spacebg, (0,0))
        sprites.draw(screen)
        asteroid_group.draw(screen)
        fueltxt = font.render("Fuel: " + str(fuel), True, (255,0,0))
        screen.blit(fueltxt, (400, 25))
        if fuel <= 0:
            pygame.quit()
            exit()
        pygame.display.update()

startGame()