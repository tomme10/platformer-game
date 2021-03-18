from Modules.object import object
import pygame
from math import sin,cos,radians
from random import randint
from Modules.collision import rect2rect
import Modules.scenes as s

screen = pygame.Rect(0,0,800,600)

class orb(object):
    def __init__(self,pos):
        self.frames = [pygame.image.load(f'Assets\\orb\\corruptedOrb{i+1}.png') for i in range(6)]
        self.index = 0
        self.time = 0

        self.rect = self.frames[0].get_rect()
        self.rect.topleft = pos

        self.spits = []

    def update(self,dtime,objects):
        self.time += dtime
        if self.time > 100:
            self.index += 1
            self.time = 0
            self.index %= len(self.frames)

        if randint(1,4) == 1:
            self.spits.append(spit(self.rect.center,radians(randint(0,360*10)/10)))

        for i,s in reversed(list(enumerate(self.spits))):
            s.update(dtime,objects)
            if s.dead:
                try:
                    del self.spits[i]
                except IndexError:
                    print(i)
        

    def draw(self,root):
        root.blit(self.frames[self.index],self.rect)
        for s in self.spits:
            s.draw(root)

    def reset(self):
        self.spits = []
        self.time = 0
        self.index = 0


class spit(object):
    def __init__(self,pos,angle):
        self.frames = [pygame.image.load(f'Assets\\spit\\spit{i+1}.png') for i in range(5)]
        self.index = 0
        self.time = 0
        self.vel = [sin(angle)*0.5,cos(angle)*0.5]
        self.rect = self.frames[0].get_rect()
        self.rect.center = pos

        self.trail = []

        self.dead = False

    def update(self,dtime,objects):
        self.time += dtime
        if self.time > 100:
            self.index += 1
            self.index %= len(self.frames)
            self.time -= 100

        self.trail.append([self.frames[self.index].copy(),self.rect.topleft])
        if len(self.trail) > 5:
            del self.trail[0]

        self.rect.move_ip(self.vel[0]*dtime,self.vel[1]*dtime)

        colliders = [obj for obj in objects if obj.collisions and obj != self]

        for collider in colliders:
            if rect2rect([self.rect.topleft,self.rect.topright,self.rect.bottomright,self.rect.bottomleft],collider.pts):
                if type(collider).__name__ == 'player':
                    s.currentScene.reset()
                else:
                    self.dead = True


        if not self.rect.colliderect(screen):
            self.dead = True

    def draw(self,root):
        root.blit(self.frames[self.index],self.rect)
        for i,img in enumerate(self.trail):
            img[0].set_alpha((255/5)*i)
            root.blit(img[0],img[1])
            #pygame.draw.rect(root,(255,0,0), (img[1], img[0].get_size()),3)

