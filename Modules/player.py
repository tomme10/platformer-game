from Modules.object import object
import pygame
from math import floor,ceil,sin,cos,sqrt,radians,degrees
import numpy as np
from Modules.collision import *

jheight = 500

gravity = 10


class player(object):

    collisions = True

    def __init__(self,x,y):
        self.orisurf = pygame.Surface((25,25))
        self.orisurf.fill((255,0,0))
        self.orisurf.set_colorkey((0,0,0,0))
        self.surf = self.orisurf.copy()
        self.x,self.y = x,y
        self.vel = [0,0]

        self.angle = 0

    def update(self,dtime,objects):
        keys = pygame.key.get_pressed()

        colliders = [obj for obj in objects if obj.collisions and obj != self]

        if keys[pygame.K_d]:
            self.vel[0] += 10
        if keys[pygame.K_a]:
            self.vel[0] -= 10
        if keys[pygame.K_w]:
            self.vel[1] -= 10
        if keys[pygame.K_s]:
            self.vel[1] += 10
        if keys[pygame.K_q]:
            self.angle += radians(1)
        if keys[pygame.K_e]:
            self.angle -= radians(1)

        x,y = self.vel
        vel = np.array([x*cos(self.angle)-y*sin(self.angle),x*sin(self.angle)+y*cos(self.angle)])
        vel *= dtime/1000

        self.x += vel[0]
        self.y += vel[1]

        self.pts = [[self.x+12.5,self.y+12.5],[self.x-12.5,self.y+12.5],[self.x-12.5,self.y-12.5],[self.x+12.5,self.y-12.5]]
        for i in range(len(self.pts)):
            pt = [self.pts[i][0]-self.x,self.pts[i][1]-self.y]
            self.pts[i] = [pt[0]*cos(self.angle)-pt[1]*sin(self.angle) , pt[0]*sin(self.angle)+pt[1]*cos(self.angle)]
            self.pts[i][0] += self.x
            self.pts[i][1] += self.y

        self.surf = pygame.transform.rotate(self.orisurf,-degrees(self.angle))
        self.rect = self.surf.get_rect()
        self.rect.center = (self.x,self.y)

        collide = self.collide(0,0,colliders)

        if collide:
            self.orisurf.fill((0,255,0))
        else:
            self.orisurf.fill((255,0,0))
        
        print(collide)
        
    def collide(self,x,y,colliders):

        for collider in colliders:
            if rect2rect(self.pts,collider.pts):
                return True
        
        return False

    def draw(self,root):
        root.blit(self.surf,self.rect)
        #pygame.draw.polygon(root,(255,255,0),self.pts,3)