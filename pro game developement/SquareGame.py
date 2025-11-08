import pygame, random
pygame.init()

s_WIDTH = 500
s_HEIGHT = 500
screen = pygame.display.set_mode((s_WIDTH, s_HEIGHT))
score = 0
clock = pygame.time.Clock()

class box(pygame.sprite.Sprite):
    def __init__(self, colour, w, h):
        super().__init__() # calls the initialising function of "box" class
        self.image = pygame.Surface([w, h])
        self.image.fill(colour)
        self.rect = self.image.get_rect()

squarelist = pygame.sprite.Group()
allsprites = pygame.sprite.Group()

for i in range(30):
    square = box("black", 20, 15)
    square.rect.x = random.randrange(s_WIDTH)
    square.rect.y = random.randrange(s_HEIGHT)
    squarelist.add(square)
    allsprites.add(square)

for i in range(20):
    esquare = box("red", 20, 15)
    esquare.rect.x = random.randrange(s_WIDTH)
    esquare.rect.y = random.randrange(s_HEIGHT)
    squarelist.add(esquare)
    allsprites.add(esquare)

player = box("blue", 20, 15)
allsprites.add(player)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
    
    screen.fill("white")
    pos = pygame.mouse.get_pos()
    player.rect.x = pos[0] # to fetch the first item (the x position of the mouse) of the pos list
    player.rect.y = pos[1]

    collisions = pygame.sprite.spritecollide(player, squarelist, True)
    for square in collisions:
        score = score + 1
        print(score)
    
    for esquare in collisions:
        score = score - 1
        print(score)
    
    allsprites.draw(screen)
    pygame.display.flip()
    clock.tick(60)

pygame.quit()