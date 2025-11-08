import pygame, random
pygame.init()

s_WIDTH = 500
s_HEIGHT = 500
screen = pygame.display.set_mode((s_WIDTH, s_HEIGHT))
score = 0
gameover = False
clock = pygame.time.Clock()

class box(pygame.sprite.Sprite):
    def __init__(self, colour, w, h):
        super().__init__() # calls the initialising function of "box" class
        self.image = pygame.Surface([w, h])
        self.image.fill(colour)
        self.rect = self.image.get_rect()

squarelist = pygame.sprite.Group()
esquarelist = pygame.sprite.Group()
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
    esquarelist.add(esquare)
    allsprites.add(esquare)

player = box("blue", 20, 15)
allsprites.add(player)
print(allsprites)
print(squarelist)
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
    
    screen.fill("white")
    pos = pygame.mouse.get_pos()
    player.rect.x = pos[0] # to fetch the first item (the x position of the mouse) of the pos list
    player.rect.y = pos[1]

    collisions = pygame.sprite.spritecollide(player, squarelist, True)
    ecollisions = pygame.sprite.spritecollide(player, esquarelist, True)
    #print(collisions)
    for square in collisions:
        score=score+1
        if score == 30:
            gameover = True
        #print(score)
    
    for esquare in ecollisions:
        score = score-1
        if score == 30:
            gameover = True
        #print(score)
    
    allsprites.draw(screen)
    font = pygame.font.Font(None, 26)
    text = font.render("Score: " + str(score), True, ("Black"))
    screen.blit(text, (10,15))
    if gameover == True:
        font = pygame.font.Font(None, 50)
        text1 = font.render("You win!", True, ("Black"))
        screen.blit(text1, (s_WIDTH/2, s_HEIGHT/2))
    pygame.display.flip()
    clock.tick(60)

pygame.quit()