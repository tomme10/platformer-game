import pygame
from Modules.object import object

class wall(object):

    collisions = True

    def __init__(self,rect):
        self.rect = rect

    def collision(self,rect):
        return self.rect.colliderect(rect)