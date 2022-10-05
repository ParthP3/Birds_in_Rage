import pygame, sys
from bird import *
from piggy import *
from collision import *
from objects import *
from pygame.locals import *
from pygame.color import THECOLORS
pygame.init()

display_surface = pygame.display.set_mode((600,400))

#Some initial variables
framerate_limit = 120
time_s = 0.0
key_e = "U"
key_f = "U"
user_done = False
mouse_button_UD = "U" elif (event.type == pygame.MOUSEBUTTONDOWN):
            mouse_button_UD = 'D'


#=========================================
#Some examples of birds and pigs 
#=========================================
x_1 =
y_1 = 
pathimg = 
bird = Bird(x_1,y_1,pathimg, pathfx)
bird_group = pygame.sprite.Group()
bird_group.add(bird)

x_2 =
y_2 = 
pathpig = 
pigfx = 
pig = Bird(x_1,y_1,pathpig, pigfx)
pig_group = pygame.sprite.Group()
pig_group.add(pig)


#==================================================
#               Main Game Loop
#==================================================
while True :
    for event in pygame.event.get ( ) :
        if event.type == pygame.QUIT :
           pygame.quit ( )
           sys.exit ( )
        elif (event.type == pygame.MOUSEBUTTONDOWN): #To control the catapult
            mouse_button_UD = 'D'
        elif (event.type == pygame.MOUSEBUTTONUP):
            mouse_button_UD = 'U'

    #pygame.display.flip ( )
    screen.blit ( background , ( 0,0 ) )#for background image
    bird_group.draw ( screen )
    pig_group.draw ( screen )
    bird_group.update()
    pig_group.update()

    """
    There's an enormous amount of flexibility with the levels in this game
    Implementations of various power ups for birds is possible
    """