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


# these are the players
myblock = Block(LBLUE, 30, 30, 50, 50)
myblock2 = Block(BLUE, 20, 20, 100, 100)
my_sprites.add(myblock)
my_sprites.add(myblock2)

# these are the walls
wall_group = pygame.sprite.Group()
# first is thickness
# 3rd number is left nad right350
# last number is moving up and down
purple2 = Block(PURPLE, 20, 490, 80, 0)
wall2 = Block(YELLOW, 400, 20, 0, 550)
wall3 = Block(YELLOW, 240, 20, 80, 480)
vertical_yellow = Block(YELLOW, 20, 300, 390, 270)
verticalY2 = Block(YELLOW, 20, 300, 300, 200)
purple_edge = Block(PURPLE, 20, 560, 0, 0)
wall6 = Block(GREEN,20, 580, 300, 20)
# wall7 = Block(PURPLE, 190, 50, 20, 500)
# wall8 = Block(YELLOW, 590, 50, 20, 500)
wall_group.add(purple2)
wall_group.add(wall2)
wall_group.add(vertical_yellow)
wall_group.add(purple_edge)
wall_group.add(wall3)
wall_group.add(verticalY2)
# wall_group.add(wall8)

# this is how the player moves and how it hits the walls
print("1")
done = False
clock = pygame.time.Clock()


def check_and_move(sprite, direction):
    # make the move for player1
    if direction == "UP":
        sprite.rect.y -= 10
    if direction == "DOWN":
        sprite.rect.y += 10
    if direction == "LEFT":
        sprite.rect.x -= 10
    if direction == "RIGHT":
        sprite.rect.x += 10
    # make the move for player 2
    if direction == "w":
        sprite.rect.y -= 10
    if direction == "s":
        sprite.rect.y += 10
    if direction == "a":
        sprite.rect.x -= 10
    if direction == "d":
        sprite.rect.x += 10
    # more  code  for other directions
    block_hits = pygame.sprite.spritecollide(sprite, wall_group, False)
    # check for collisions
    if len(block_hits) > 0:
        # returns the block to its spawn point (currently 30,30)
        sprite.rect.x = 30
        sprite.rect.y = 30


while not done:
    #quitting thing
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
    #create the list of keypressed (bool)        
    keysPressed = pygame.key.get_pressed()
    
    #run through the list and check keys by their ID and run the function for them
    if keysPressed[pygame.K_UP]:
        check_and_move(myblock, "UP")
    if keysPressed[pygame.K_DOWN]:
        check_and_move(myblock, "DOWN")
    if keysPressed[pygame.K_LEFT]:
        check_and_move(myblock, "LEFT")
    if keysPressed[pygame.K_RIGHT]:
        check_and_move(myblock, "RIGHT")
    if keysPressed[pygame.K_w]:
        check_and_move(myblock2, "w")
    if keysPressed[pygame.K_s]:
        check_and_move(myblock2, "s")
    if keysPressed[pygame.K_a]:
        check_and_move(myblock2, "a")
    if keysPressed[pygame.K_d]:
        check_and_move(myblock2, "d")
    
    #screen update thingy
    screen.fill(WHITE)
    my_sprites.draw(screen)
    wall_group.draw(screen)

    # update
    my_sprites.update()
    pygame.display.flip()
    clock.tick(60)
pygame.quit()
