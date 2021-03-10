import pygame
from Modules.object import object

class wall(object):

    collisions = True
    drawOrder = 1

    def __init__(self,rect):
        self.pts = [rect.topleft,rect.topright,rect.bottomright,rect.bottomleft]

    def collision(self,rect):
        return self.rect.colliderect(rect)
    
    def draw(self,root):
        #pygame.draw.polygon(root,(0,0,255),self.pts,3)
        pass