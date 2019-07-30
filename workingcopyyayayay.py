import pygame

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
size = (800, 600)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
PURPLE = (255, 0, 255)
YELLOW = (255, 255, 0)
LBLUE = (173, 216, 230)
BLUE = (0, 0, 255)
speed1 = 3
running = True
direction = 0

pygame.init()
screen = pygame.display.set_mode(size)
pygame.display.set_caption("please work")
my_sprites = pygame.sprite.Group()


class Block(pygame.sprite.Sprite):
    def __init__(self, color, width, height, x, y):
        super().__init__()

        self.image = pygame.Surface([width, height])
        self.image.fill(color)

        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y


class Wall(pygame.sprite.Sprite):
    def __init__(self, color, width, height, x, y):
        super().__init__()

        self.image = pygame.Surface([width, height])
        self.image.fill(color)

        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

#these are the players
myblock = Block(LBLUE, 30, 30, 50, 50)
myblock2 = Block(BLUE, 20, 20, 100, 100)
my_sprites.add(myblock)
my_sprites.add(myblock2)

#these are the walls
wall_group = pygame.sprite.Group()
#first is thickness
# thried number is left nad right
# last number is moving up and down
wall = Block(PURPLE, 20, 490, 80, 0)
wall2 = Block(YELLOW, 400, 20, 0, 550)
wall3 = Block(BLACK, 500, 400, 400, 500)
#wall4 = Block(YELLOW, 60, 350, 200, 25)
wall5 = Block(PURPLE, 20, 550, 0,0)
# wall6 = Block(YELLOW,20, 580, 760, 20)
# wall7 = Block(PURPLE, 190, 50, 20, 500)
# wall8 = Block(YELLOW, 590, 50, 20, 500)
wall_group.add(wall)
wall_group.add(wall2)
wall_group.add(wall3)
#wall_group.add(wall4)
wall_group.add(wall5)
# wall_group.add(wall6)
# wall_group.add(wall7)
# wall_group.add(wall8)




#this is how the player moves and how it hits the walls

print("1")
done = False
clock = pygame.time.Clock()

def check_and_move(sprite, direction):
    # make the move
    if direction == "UP":
        sprite.rect.y -= 10
    if direction == "DOWN":
        sprite.rect.y += 10
    if direction == "LEFT":
        sprite.rect.x -= 10
    if direction == "RIGHT":
        sprite.rect.x += 10
    # more  code  for other directions
    block_hits = pygame.sprite.spritecollide(sprite, wall_group, False)
    # check for collisions
    if len(block_hits) > 0:
        if direction == "UP":
            sprite.rect.y += 10
        if direction == "DOWN":
            sprite.rect.y -= 10
        if direction == "LEFT":
            sprite.rect.x += 10
        if direction == "RIGHT":
            sprite.rect.x -= 10




        if direction == "w":
            sprite.rect.y += 10
        if direction == "s":
            sprite.rect.y -= 10
        if direction == "a":
            sprite.rect.x += 10
        if direction == "d":
            sprite.rect.x -= 10
            # more  code  for other directions
        block_hits = pygame.sprite.spritecollide(sprite, wall_group, False)
        # check for collisions
        if len(block_hits) > 0:
            if direction == "w":
                sprite.rect.y += 10
            if direction == "s":
                sprite.rect.y -= 10
            if direction == "a":
                sprite.rect.x += 10
            if direction == "d":
                sprite.rect.x -= 10



while not done:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

    print("2")
    if event.type == pygame.KEYDOWN:
        if event.key == pygame.K_UP:
            check_and_move(myblock, "UP")
        if event.key == pygame.K_DOWN:
            check_and_move(myblock, "DOWN")
        if event.key == pygame.K_LEFT:
            check_and_move(myblock, "LEFT")
        if event.key == pygame.K_RIGHT:
            check_and_move(myblock, "RIGHT")




    if event.type == pygame.KEYDOWN:
        if event.key == pygame.K_w:
            check_and_move(myblock2, "w")
        if event.key == pygame.K_s:
            check_and_move(myblock2, "s")
        if event.key == pygame.K_a:
            check_and_move(myblock2, "a")
        if event.key == pygame.K_d:
            check_and_move(myblock2, "d")












    screen.fill(WHITE)
    my_sprites.draw(screen)
    wall_group.draw(screen)


    # update
    my_sprites.update()
    pygame.display.flip()
    clock.tick(60)
pygame.quit()
