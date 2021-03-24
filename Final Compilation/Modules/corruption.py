from Modules.object import object
import pygame
from math import sin,cos,radians
from random import randint
from Modules.collision import rect2rect
import Modules.scenes as s

screen = pygame.Rect(0,0,800,600)

class orb(object):
    def __init__(self,pos,chance = 3):
        self.frames = [pygame.image.load(f'Assets\\orb\\corruptedOrb{i+1}.png') for i in range(6)]
        self.index = 0
        self.time = 0

        self.chance = chance

        self.rect = self.frames[0].get_rect()
        self.rect.topleft = pos

        self.spits = []

    def update(self,dtime,objects):
        self.time += dtime
        if self.time > 100:
            self.index += 1
            self.time = 0
            self.index %= len(self.frames)

        if randint(1,self.chance) == 1:
            self.spits.append(spit(self.rect.center,radians(randint(0,360*100)/100)))

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
        for i,img in enumerate(self.trail):
            img[0].set_alpha((255/5)*i)
            root.blit(img[0],img[1])

        root.blit(self.frames[self.index],self.rect)


class corruptionWall(object):
    drawOrder = 2
    def __init__(self,time = 10000):
        self.frames = [pygame.image.load(f'Assets\\corruption\\transition{i+1}.png') for i in range(6)]
        self.y = 0
        self.rect = self.frames[0].get_rect()
        self.rect.centerx = 400
        self.rect.bottom = self.y
        self.time = 0
        self.endTime = time
        self.transitionTime = 0

        self.pts = [self.rect.topleft,self.rect.topright,(self.rect.right,self.rect.bottom+25),(self.rect.left,self.rect.bottom+25)]

        self.ind = 0

    def update(self,dtime,objects):
        self.time += dtime
        if self.time > self.endTime:
            self.transitionTime += dtime
            self.y = (600/5000)*self.transitionTime
        else:
            self.y = -1000

        if 0 < self.time%100 < 20:
            self.ind += 1
            self.ind %= len(self.frames)

        self.rect.bottom = self.y

        self.pts = [self.rect.topleft,self.rect.topright,(self.rect.right,self.rect.bottom+25),(self.rect.left,self.rect.bottom+25)]

    def draw(self,root):
        root.blit(self.frames[self.ind],self.rect)
        #pygame.draw.polygon(root,(255,0,0),self.pts,3)

    def reset(self):
        self.y = 0
        self.rect.bottom = self.y
        self.time = 0
        self.transitionTime = 0

class flames(object):
    def __init__(self,x,y):
        self.frames = [pygame.image.load(f'Assets\\flames\\flames{i+1}.png') for i in range(7)]
        self.index = randint(0,6)
        self.time = 0
        self.rect = self.frames[0].get_rect()
        self.rect.topleft = (x,y)

    def update(self,dtime,objects):
        
        self.time += dtime
        if self.time > 100:
            self.time -= 100
            self.index += 1
            self.index %= len(self.frames)

    def draw(self,root):
        root.blit(self.frames[self.index],self.rect)