from Modules.object import object
from math import sin,cos,radians,degrees
from Modules.collision import rect2rect
import pygame

class portal(object):

    def __init__(self,p1,angle):
        self.surf = pygame.image.load('Assets\\gravPortal.png')
        self.angle = radians(angle)
        print(angle)
        self.pos = p1
        self.surf = pygame.transform.rotate(self.surf,degrees(self.angle))
        self.pts = [p1,(p1[0]+sin(self.angle+radians(90))*100,p1[1]+cos(self.angle+radians(90))*100)]

    def update(self,dtime,objects):

        for obj in objects:
            if type(obj).__name__ == 'player':
                if rect2rect(self.pts+[self.pts[1],self.pts[0]],obj.pts):
                    obj.angle = self.angle

    def draw(self,root):
        #pygame.draw.line(root,(0,0,255),self.pts[0],self.pts[1],3)
        pass