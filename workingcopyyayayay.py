import pygame

BLACK = (0,0,0)
WHITE = (255,255,255)
BLUE = (0,0,255)
RED = (255,0,0)
size = (700,500)
speed1= 3
running = True

# initialize pygame and window
pygame.init()
screen = pygame.display.set_mode(size)
pygame.display.set_caption("demo")
# set up sprites
my_sprites = pygame.sprite.Group()

class Block(pygame.sprite.Sprite):
    def __init__(self, color, width, height, x, y):
        super().__init__()

        self.image = pygame.Surface([width, height])
        self.image.fill(color)

        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

BLUE = (0,0,255)
myblock = Block(BLUE, 30, 30, 50, 50)
myblock2 = Block(BLUE, 20, 20, 100, 100)
my_sprites.add(myblock)
my_sprites.add(myblock2)

print("1")
done = False
clock = pygame.time.Clock()
# main loop
while not done:
    #event catcher
    for event in pygame.event.get():
        # abort sequence
        if event.type == pygame.QUIT:
            done = True
    print("2")
    if event.type == pygame.KEYDOWN:
        if event.key == pygame.K_UP:
            myblock.rect.y += -10
        if event.key == pygame.K_DOWN:
            myblock.rect.y += 10
        if event.key == pygame.K_LEFT:
            myblock.rect.x += -10
        if event.key == pygame.K_RIGHT:
            myblock.rect.x += 10

    print("3")
    if event.type == pygame.KEYDOWN:
        if event.key == pygame.K_w:
            myblock2.rect.y += -10
        if event.key == pygame.K_s:
            myblock2.rect.y += 10
        if event.key == pygame.K_a:
            myblock2.rect.x += -10
        if event.key == pygame.K_d:
            myblock2.rect.x += 10




    #logic

    # draw
    screen.fill(WHITE)
    my_sprites.draw(screen)

    # update
    my_sprites.update()
    pygame.display.flip()
    clock.tick(60)
pygame.quit()
