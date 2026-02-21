import pygame

pygame.init()
WIDTH = 600
HEIGHT = 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Rocket Game")

class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("rocket.png").convert_alpha()
        self.image = pygame.transform.scale(self.image, (70,100))
        self.rect = self.image.get_rect() #creates hitbox for collision, movement detection and other events
    
    def update(self, pressed_keys):
        if pressed_keys[pygame.K_UP]:
            self.rect.move_ip(0, -5) #moves 0 pixels horizontally and 5 pixels up vertically (move.ip means move in place)
        
        if pressed_keys[pygame.K_DOWN]:
            self.rect.move_ip(0, 5)
        
        if pressed_keys[pygame.K_LEFT]:
            self.rect.move_ip(-5, 0)
        
        if pressed_keys[pygame.K_RIGHT]:
            self.rect.move_ip(5, 0)
        
        #Setting screen boundary for player
        if self.rect.left < 0:
            self.rect.left = 0
        
        elif self.rect.right > WIDTH:
            self.rect.right = WIDTH
        
        elif self.rect.top <= 0:
            self.rect.top = 0
        
        elif self.rect.bottom >= HEIGHT:
            self.rect.bottom = HEIGHT

sprites = pygame.sprite.Group()
def startGame():
    player = Player()
    sprites.add(player)
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()

        pressed_keys = pygame.key.get_pressed()
        player.update(pressed_keys)
        Spacebg_img = pygame.image.load("SpaceGamebg.jpg")
        Spacebg = pygame.transform.scale(Spacebg_img, (WIDTH, HEIGHT))
        screen.blit(Spacebg, (0,0))
        sprites.draw(screen)
        pygame.display.update()

startGame()