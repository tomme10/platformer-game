import pygame
from Modules.object import object

class img(object):

    def __init__(self,surf,center = (400,300),wh = None):
        self.surf = surf
        if wh:
            self.surf = pygame.transform.scale(self.surf, wh)

        self.rect = self.surf.get_rect()
        self.rect.center = center

    def update(self,dtime,objects):pass
    
    def draw(self,root):
        root.blit(self.surf,self.rect)