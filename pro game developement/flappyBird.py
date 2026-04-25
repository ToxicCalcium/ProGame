import pygame, random

pygame.init()
WIDTH = 400
HEIGHT = 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()

class bird:
    def __init__(self):
        self.x = 80
        self.y = 300
        self.vel = 0
    
    def jump(self):
        self.vel = -10

    def birdmove(self):
        self.vel += 0.5
        self.y += self.vel

    def draw(self):
        pygame.draw.circle(screen, (255, 255, 0), (self.x, int(self.y)), 15)

class pipe:
    def __init__(self):
        self.x = 400
        self.height = random.randint(115, 400)
    
    def move(self):
        self.x -= 4
    
    def draw(self):
        pygame.draw.rect(screen, (0, 255, 0), (self.x, 0, 50, self.height - 80))
        pygame.draw.rect(screen, (0, 255, 0), (self.x, self.height+80, 50, 600))
    
    def collide(self, bird):
        if bird.x + 15 > self.x and bird.x - 15 < self.x + 50:
            if bird.y - 15 < self.height - 80 or bird.y + 15 > self.height + 80:
                return True
        return False

flappyBird = bird()
greenPipe = pipe()
running = True
while running: 
    clock.tick(60)
    screen.fill((0, 0, 255))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                flappyBird.jump()
    flappyBird.birdmove()
    greenPipe.move()
    if greenPipe.x < -50:
        greenPipe = pipe()
    if greenPipe.collide(flappyBird) or flappyBird.y > HEIGHT:
        running = False
    
    flappyBird.draw()
    greenPipe.draw()

    pygame.display.update()

pygame.quit()