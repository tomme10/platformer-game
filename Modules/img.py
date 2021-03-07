import pygame
from Modules.object import object

class img(object):

    def __init__(self,surf,center = (400,300)):
        self.surf = surf
        self.rect = self.surf.get_rect()
        self.rect.center = center
        self.x = 0
        self.rect.centerx = self.x

    def update(self,dtime,objects):
        self.x += 10*(dtime/1000)
        self.rect.centerx = self.x
    
    def draw(self,root):
        root.blit(self.surf,self.rect)