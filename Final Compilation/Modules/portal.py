from Modules.object import object
from math import sin,cos,radians,degrees
from Modules.collision import rect2rect
import pygame

class portal(object):

    def __init__(self,p1,angle):
        self.frames = [pygame.image.load(f'Assets\\gravPortal\\gravPortal{i+1}.png') for i in range(8)]
        for i,frame in enumerate(self.frames):
            self.frames[i] = pygame.transform.rotate(frame,-angle)

        self.index = 0
        self.time = 0
        self.surf = self.frames[0]

        self.angle = radians(angle)

        self.rect = self.surf.get_rect()
        self.rect.center = p1

        self.pts = [(p1[0]-sin(-self.angle+radians(90))*50,p1[1]-cos(-self.angle+radians(90))*50),(p1[0]+sin(-self.angle+radians(90))*50,p1[1]+cos(-self.angle+radians(90))*50)]

    def update(self,dtime,objects):

        for obj in objects:
            if type(obj).__name__ == 'player':
                if rect2rect(self.pts+[self.pts[1],self.pts[0]],obj.pts):
                    obj.angle = self.angle

        self.time += dtime
        if self.time > 100:
            self.time -= 100
            self.index += 1
            self.index %= len(self.frames)

            self.surf = self.frames[self.index]

    def draw(self,root):
        root.blit(self.surf,self.rect)
        #pygame.draw.polygon(root, (0,0,255), self.pts+self.pts,3)
        #pygame.draw.rect(root,(0,255,0),self.rect,4)
        #pygame.draw.circle(root,(0,255,0),self.rect.center,10)
        pass