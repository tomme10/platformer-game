from Modules.object import object
import pygame
from math import floor,ceil,sin,cos,sqrt,radians,degrees
import numpy as np
from Modules.collision import *

jheight = 500

gravity = 10


class player(object):

    collisions = True
    angle = 0

    def __init__(self,x,y):
        self.orisurf = pygame.Surface((25,25))
        self.orisurf.fill((255,0,0))
        self.orisurf.set_colorkey((0,0,0,0))
        self.surf = self.orisurf.copy()
        self.x,self.y = x,y
        self.vel = [0,0]

        self.pts = [[self.x+12.5,self.y+12.5],[self.x-12.5,self.y+12.5],[self.x-12.5,self.y-12.5],[self.x+12.5,self.y-12.5]]
        for i in range(len(self.pts)):
            pt = [self.pts[i][0]-self.x,self.pts[i][1]-self.y]
            self.pts[i] = [pt[0]*cos(self.angle)-pt[1]*sin(self.angle) , pt[0]*sin(self.angle)+pt[1]*cos(self.angle)]
            self.pts[i][0] += self.x
            self.pts[i][1] += self.y

        self.angle = 0

    def update(self,dtime,objects):
        keys = pygame.key.get_pressed()

        colliders = [obj for obj in objects if obj.collisions and obj != self]

        onFloor = self.collide(0,0,colliders)

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

        if not onFloor:
            self.vel[1] += 10
        elif self.vel[1] > 0:
            print(onFloor)
            self.vel[1] = 0

        vel = [self.vel[0]*(dtime/1000),self.vel[1]*(dtime/1000)]

        print(self.collide(1,0,colliders),self.collide(-10000,0,colliders))

        if self.collide(vel[0],vel[1],colliders):
            while self.collide(vel[0],0,colliders):
                if vel[0] > 1:
                    vel[0] -= 1
                elif vel[0] < -1:
                    vel[0] += 1
                else:
                    vel[0] = 0

                    if not self.collide(vel[0],-1*vel[0],colliders):
                        off = 0
                        while not self.collide(vel[0],-1*vel[0]-off,colliders):
                            off += 1
                        
                        vel[1] = -1*vel[0]-off

                    break

            while self.collide(0,vel[1],colliders):
                if vel[1] > 1:
                    vel[1] -= 1
                elif vel[1] < -1:
                    vel[1] += 1
                else:
                    vel[1] = 0
                    break

        #print(self.collide(vel[0],0,colliders),self.collide(0,vel[1],colliders),self.collide(vel[0],vel[1],colliders))

        x,y = vel
        #if vel[0] > 0:
        #    self.vel[0] = floor(vel[0]/(dtime/1000))
        #else:
        #    self.vel[0] = ceil(vel[0]/(dtime/1000))

        #if vel[1] > 0:
        #    self.vel[1] = floor(vel[1]/(dtime/1000))
        #else:
        #    self.vel[1] = ceil(vel[1]/(dtime/1000))

        self.vel = [vel[0]/(dtime/1000),vel[1]/(dtime/1000)]

        vel = np.array([x*cos(self.angle)-y*sin(self.angle),x*sin(self.angle)+y*cos(self.angle)])

        self.x += vel[0]
        self.y += vel[1]

        self.surf = pygame.transform.rotate(self.orisurf,degrees(self.angle))
        self.rect = self.surf.get_rect()
        self.rect.center = (self.x,self.y)

        self.pts = [[self.x+12.5,self.y+12.5],[self.x-12.5,self.y+12.5],[self.x-12.5,self.y-12.5],[self.x+12.5,self.y-12.5]]
        for i in range(len(self.pts)):
            pt = [self.pts[i][0]-self.x,self.pts[i][1]-self.y]
            self.pts[i] = [pt[0]*cos(self.angle)-pt[1]*sin(self.angle) , pt[0]*sin(self.angle)+pt[1]*cos(self.angle)]
            self.pts[i][0] += self.x
            self.pts[i][1] += self.y

    def collide(self,x,y,colliders):

        vel = np.array([x*cos(self.angle)-y*sin(self.angle),x*sin(self.angle)+y*cos(self.angle)])

        pts = self.pts.copy()

        for point in pts:
            point[0] += vel[0]
            point[1] += vel[1]

        for collider in colliders:
            if rect2rect(pts,collider.pts):
                return True
        
        return False

    def draw(self,root):
        root.blit(self.surf,self.rect)
        #pygame.draw.polygon(root,(255,255,0),self.pts,3)