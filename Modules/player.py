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

    drawOrder = 2

    def __init__(self,x,y,angle = 0):
        self.orisurf = pygame.Surface((25,25))
        self.orisurf.fill((255,0,0))
        self.orisurf.set_colorkey((0,0,0,0))
        self.surf = self.orisurf.copy()
        self.x,self.y = x,y
        self.vel = [0,0]

        self.oripos = [self.x,self.y]
        self.oriAngle = angle

        self.rect = self.surf.get_rect()
        self.rect.center = [self.x,self.y]

        self.pts = [[self.x+12.5,self.y+12.5],[self.x-12.5,self.y+12.5],[self.x-12.5,self.y-12.5],[self.x+12.5,self.y-12.5]]
        for i in range(len(self.pts)):
            pt = [self.pts[i][0]-self.x,self.pts[i][1]-self.y]
            self.pts[i] = [pt[0]*cos(self.angle)-pt[1]*sin(self.angle) , pt[0]*sin(self.angle)+pt[1]*cos(self.angle)]
            self.pts[i][0] += self.x
            self.pts[i][1] += self.y

        self.angle = angle

    def update(self,dtime,objects):
        keys = pygame.key.get_pressed()
        colliders = [obj for obj in objects if obj.collisions and obj != self]

        # keys and movement
        self.vel[0] = 0
        if keys[pygame.K_d]:
            self.vel[0] += 175
        if keys[pygame.K_a]:
            self.vel[0] -= 175
        if keys[pygame.K_q]:
            self.angle -= radians(5)
        if keys[pygame.K_e]:
            self.angle += radians(5)

        if self.collide(0,1,colliders) and keys[pygame.K_SPACE]:
            self.vel[1] = -500

        self.vel[1] += 10

        #self.vel[1] += 10
    
        # vel dampening
        vel = [self.vel[0]*(dtime/1000),self.vel[1]*(dtime/1000)]

        climb = False

        if self.collide(vel[0],0,colliders):
            if not self.collide(vel[0],-abs(vel[0]),colliders):
                climb = True
                while self.collide(vel[0],vel[1],colliders):
                    vel[1] -= 1
            
            else:
                while self.collide(vel[0],0,colliders):
                    if vel[0] > 1:
                        vel[0] -= 1
                    elif vel[0] < -1:
                        vel[0] += 1
                    else:
                        vel[0] = 0
                        break


        if not climb:
            while self.collide(vel[0],vel[1],colliders):
                if vel[1] > 1:
                    vel[1] -= 1
                elif vel[1] < -1:
                    vel[1] += 1
                else:
                    vel[1] = 0
                    break

        self.vel = [vel[0]/(dtime/1000),vel[1]/(dtime/1000)]
        # rotate vel
        v = [vel[0]*cos(self.angle)-vel[1]*sin(self.angle),vel[0]*sin(self.angle)+vel[1]*cos(self.angle)]

        # apply vel
        self.x += v[0]
        self.y += v[1]

        #if climb and self.vel[1] < 0:
        #    self.vel[1] = 0

        # rotate surf, + create/move rect
        self.surf = pygame.transform.rotate(self.orisurf,180-degrees(self.angle))
        self.rect = self.surf.get_rect()
        self.rect.center = (self.x,self.y)

        # update points
        self.pts = [[self.x+12.5,self.y+12.5],[self.x-12.5,self.y+12.5],[self.x-12.5,self.y-12.5],[self.x+12.5,self.y-12.5]]
        for i in range(len(self.pts)):
            pt = [self.pts[i][0]-self.x,self.pts[i][1]-self.y]
            self.pts[i] = [pt[0]*cos(self.angle)-pt[1]*sin(self.angle) , pt[0]*sin(self.angle)+pt[1]*cos(self.angle)]
            self.pts[i][0] += self.x
            self.pts[i][1] += self.y

        # object interactions
        #for obj in objects:
        #    if type(obj).__name__ == 'orb':
        #        for spit in orb.spits:
        #            if rect2rect(spit)


    def collide(self,x,y,colliders):

        v = [x*cos(self.angle)-y*sin(self.angle),x*sin(self.angle)+y*cos(self.angle)]

        points = []
        for point in self.pts:
            points.append([point[0],point[1]])
        

        for point in points:
            point[0] += v[0]
            point[1] += v[1]

        for collider in colliders:
            if rect2rect(points,collider.pts):
                del points,v,x,y
                return True
        
        del points,v,x,y
        return False

    def draw(self,root):
        root.blit(self.surf,self.rect)
        #pygame.draw.polygon(root,(255,255,0),self.pts,3)

    def reset(self):
        self.x,self.y = self.oripos.copy()
        self.angle = self.oriAngle

        self.vel = [0,0]

        self.pts = [[self.x+12.5,self.y+12.5],[self.x-12.5,self.y+12.5],[self.x-12.5,self.y-12.5],[self.x+12.5,self.y-12.5]]
        for i in range(len(self.pts)):
            pt = [self.pts[i][0]-self.x,self.pts[i][1]-self.y]
            self.pts[i] = [pt[0]*cos(self.angle)-pt[1]*sin(self.angle) , pt[0]*sin(self.angle)+pt[1]*cos(self.angle)]
            self.pts[i][0] += self.x
            self.pts[i][1] += self.y

