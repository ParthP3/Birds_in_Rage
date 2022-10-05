import pygame, sys


class Bird(pygame.sprite.Sprite):
    def __init__(self, bird_x,bird_y, bird_picture_path, bird_fx_path):
        super().__init__()
        self.image
        self.img_rect = self.image.get_rect()
        self.img_rect.center = [bird_x, bird_y] 
        self.soundfx 
        pass
    def locate(self):
        return self.img_rect.center
    def collide(self, group_name):
        self.soundfx.play() 
        pygame.sprite.spritecollide(Bird,group_name,True)#true or false, second one disappears
        #technically it should be false
        pass

class Piggy(pygame.sprite.Sprite) :
    def __init__(self, pig_x,pig_y, pig_picture_path, pig_fx_path):
        super().__init__()
        self.image 
        self.img_rect = self.image.get_rect()
        self.img_rect.center = [pig_x, pig_y] 
        self.soundfx
        pass
    def locate(self):
        return self.img._rect.center
    def collide(self, group_name):
        self.soundfx.play() 
        pygame.sprite.spritecollide(Piggy,group_name,True)#true or false, second one disappears
        pass

#===========================================================
#              Add obstacles and other objects
#===========================================================


