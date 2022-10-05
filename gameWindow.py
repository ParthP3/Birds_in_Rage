import pygame, sys
from objects import *
from collision import *
from pygame.locals import *
from pygame.color import THECOLORS

class GameWindow:
    def __init__(self, screen_tuple_px):
        self.width__in_px = screen_tuple_px[0]
        self.height__in_px = screen_tuple_px[1]

        self.surface = pygame.display.set_mode(screen_tuple_px)
        
        # Paint screen black.
        self.erase_and_update()
        
    def update_caption(self, title):
        pygame.display.set_caption(title)
        self.caption = title
        
    def erase_and_update(self):
        # Useful for shifting between the various demos.
        self.surface.fill(THECOLORS["black"])
        pygame.display.flip()