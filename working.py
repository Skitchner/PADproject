
import pygame
import sys
import time
pygame.init()

color1 = pygame.Color(255,90,110) #define the colour pink w its RGB values

size = width,height=320,240 #save the size we want
screen = pygame.display.set_mode(size) #initialise the screen to the saved size

speed = [2,2] #define the speed of our ball
ball = pygame.Surface([20,20])
ball.image.fill(225,0,234)
ballrect=ball.get_rect() #gets the dimensions (hitbox) of the ball

while True:
   for event in pygame.event.get():
       if event.type == pygame.QUIT:
           quit()
   #quitting algorithm thingy ^

   ballrect=ballrect.move(speed) #move the ball at its speed

   if  ballrect.left <0 or ballrect.right > width:
       speed[0] = -speed[0]
   if  ballrect.top <0 or ballrect.bottom > height:
       speed[1] = -speed[1]
   #if statements that switch direction if we hit the wall of the screen

   screen.fill(color1) #makes screen pink
   screen.blit(ball,ballrect) #draws ball to ballrect pos
   pygame.display.flip() #not sure yet i think it updates the screen
   time.sleep(.01) #delays a thing