import pygame
from Modules.object import object

class wall(object):

    collisions = True
    drawOrder = 1

    def __init__(self,rect):
        self.rect = rect

    def collision(self,rect):
        return self.rect.colliderect(rect)
    
    def draw(self,root):
        #pygame.draw.rect(root,(255,255,0),self.rect,3)
        pass