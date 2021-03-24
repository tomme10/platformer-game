import pygame
from Modules.object import object

class wall(object):

    collisions = True
    drawOrder = 1

    def __init__(self,pts):
        self.pts = pts.copy()

    def collision(self,rect):
        return self.rect.colliderect(rect)
    
    def draw(self,root):
        #pygame.draw.polygon(root,(0,0,255),self.pts,2)
        pass