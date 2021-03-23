from Modules.object import object
from math import sqrt,sin,cos,radians
import pygame

class flag(object):

    touching = False

    def __init__(self,x,y,angle):
        self.x = x
        self.y = y
        self.x -= sin(radians(angle))
        self.y -= cos(radians(angle))
        self.cx = x+20
        self.cy = y+20

        self.surf = pygame.image.load('Assets\\portal\\flag.png')
        self.surf = pygame.transform.rotate(self.surf,-angle)
        self.surf.set_colorkey((0,0,0))

    def update(self,dtime,objects):

        for obj in objects:
            if type(obj).__name__ == 'player':
                if sqrt((obj.x-self.cx)**2+(obj.y-self.cy)**2) < 22.5:
                    self.touching = True
                else:
                    self.touching = False
                break

    def draw(self,root):
        root.blit(self.surf,(self.x,self.y))
        