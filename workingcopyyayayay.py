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
        if color == LBLUE:
            big_image = pygame.image.load("/Users/sarahkitchner/Downloads/redracecar.png")
            self.image = pygame.transform.scale(big_image, (width, height))
        if color == BLUE:
            small_image = pygame.image.load("/Users/sarahkitchner/Downloads/blueracecar.png")
            self.image = pygame.transform.scale(small_image, (width, height))

        # self.image.fill(color)

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


class movingWall(Wall):
    def __init__(self,color,width,height,x,y,yspeed,xspeed,wallBound):
        Wall.__init__(self,color,width,height,x,y)
        self.direction = direction
        self.distanceMoved=yspeed
        self.yspeed=yspeed
        self.xspeed=xspeed
        self.wallBound = wallBound
    def updateMovement(self):
        self.rect.y += self.yspeed
        self.distanceMoved += self.yspeed
        if abs(self.distanceMoved) > self.wallBound:
            self.distanceMoved = 0
            self.yspeed = self.yspeed * -1


# these are the players
myblock = Block(LBLUE, 20, 20, 55, 50)
myblock2 = Block(BLUE, 20, 20, 25, 50)
my_sprites.add(myblock)
my_sprites.add(myblock2)
# these are the walls
wall_group = pygame.sprite.Group()
# first is thickness
# 3rd number is left nad right350
# last number is moving up and down
purple2 = Wall(PURPLE, 20, 500, 80, 0)
wall2 = Wall(YELLOW, 400, 20, 0, 550)
wall3 = Wall(YELLOW, 240, 20, 80, 480)
side3 = Wall(BLACK, 800, 20, 0, -10)
vertical_yellow = Wall(YELLOW, 20, 300, 390, 270)
verticalY2 = Wall(YELLOW, 20, 300, 300, 200)
purple_edge = Wall(PURPLE, 20, 560, 0, 0)
wall6 = Wall(GREEN, 20, 580, 300, 20)
side1 = Wall(BLACK, 20, 700, -10, 0)
side2 = Wall(BLACK, 20, 700, 785, 0)
side_Y2m = Wall(GREEN, 300,20, 300, 190)
side_Y3 = Wall(GREEN, 250, 20, 390, 250)
movingWall1 = movingWall(BLUE,20,20,450,175,1,0,100)
# wall8 = Block(YELLOW, 590, 50, 20, 500)
wall_group.add(purple2)
wall_group.add(wall2)
wall_group.add(vertical_yellow)
wall_group.add(purple_edge)
wall_group.add(wall3)
wall_group.add(verticalY2)
wall_group.add(side1)
wall_group.add(side2)
wall_group.add(side3)
wall_group.add(side_Y2m)
wall_group.add(side_Y3)
wall_group.add(movingWall1)


Winners_spot = pygame.sprite.Group()

end = Wall(RED, 200, 50, 600, 560)

Winners_spot.add(end)

# this is how the player moves and how it hits the walls
print("1")
done = False
clock = pygame.time.Clock()


def check_and_move(sprite):
    # make the move for the relevant sprite
    sprite.rect.y += sprite.yspeed
    sprite.rect.x += sprite.xspeed
    block_hits = pygame.sprite.spritecollide(sprite, wall_group, False)
    # check for collisions
    if len(block_hits) > 0:
        # returns the block to its spawn point (currently 30,30)
        sprite.rect.x = 30
        sprite.rect.y = 30
        sprite.xspeed = 0
        sprite.yspeed = 0


def victory_wall(sprite):
    victory_hit = pygame.sprite.spritecollide(sprite, Winners_spot, False)
    # check for collisions
    if len(victory_hit) > 0:
        print("VICTORY")


while not done:
    # quitting thing
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
    # create the list of keyPressed (bool)
    keysPressed = pygame.key.get_pressed()
    gameSpeed = 1
    # run through the list and check keys by their ID and run the function for them
    if keysPressed[pygame.K_UP]:
        myblock.yspeed -= gameSpeed
    elif keysPressed[pygame.K_DOWN]:
        myblock.yspeed += gameSpeed
    else:
        myblock.yspeed = 0

    if keysPressed[pygame.K_LEFT]:
        myblock.xspeed -= gameSpeed
    elif keysPressed[pygame.K_RIGHT]:
        myblock.xspeed += gameSpeed
    else:
        myblock.xspeed = 0

    if keysPressed[pygame.K_w]:
        myblock2.yspeed -= gameSpeed
    elif keysPressed[pygame.K_s]:
        myblock2.yspeed += gameSpeed
    else:
        myblock2.yspeed = 0

    if keysPressed[pygame.K_a]:
        myblock2.xspeed -= gameSpeed
    elif keysPressed[pygame.K_d]:
        myblock2.xspeed += gameSpeed
    else:
        myblock2.xspeed = 0

    check_and_move(myblock)
    check_and_move(myblock2)
    movingWall1.updateMovement()
    victory_wall(myblock)
    victory_wall(myblock2)
    screen.fill(WHITE)
    my_sprites.draw(screen)
    wall_group.draw(screen)
    Winners_spot.draw(screen)

    # update
    my_sprites.update()
    pygame.display.flip()
    clock.tick(60)
pygame.quit()
