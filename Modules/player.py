from Modules.object import object
import pygame


def divis(x,y):
    if y == 0:
        return 10
    else:
        return (x/y)/10

gravity = 10

class player(object):

    collisions = True

    def __init__(self,x,y):
        self.surf = pygame.Surface((25,25))
        self.surf.fill((255,0,0))
        self.x,self.y = x,y
        self.vel = [0,0]
        self.rect = self.surf.get_rect()
        self.rect.center = (self.x,self.y)

    def update(self,dtime,objects):

        colliders = [obj for obj in objects if obj.collisions and obj != self]

        onfloor = self.collide(0,5,colliders)

        self.vel[1] += gravity
        self.vel[1] = min(self.vel[1],250)

        keys = pygame.key.get_pressed()

        self.vel[0] = 0

        if onfloor:
            self.vel[1] = 0
            if keys[pygame.K_SPACE]:
                self.vel[1] -= 250

        if keys[pygame.K_d]:
            self.vel[0] += 100
        if keys[pygame.K_a]:
            self.vel[0] -= 100

        vel = [self.vel[0]*(dtime/1000),self.vel[1]*(dtime/1000)]

        if self.collide(vel[0],vel[1],colliders):
            while self.collide(vel[0],0,colliders):
                if vel[0] > 1:
                    vel[0] -= 1
                elif vel[0] < -1:
                    vel[0] += 1
                else:
                    vel[0] = 0
                    break

            while self.collide(0,vel[1],colliders):
                if vel[1] > 0.5:
                    vel[1] -= 0.5
                elif vel[1] < -0.5:
                    vel[1] += 0.5
                else:
                    vel[1] = 0
                    break

        self.vel[0] = vel[0]/(dtime/1000)
        self.vel[1] = vel[1]/(dtime/1000)

        self.x += vel[0]
        self.y += vel[1]

        self.rect.center = (self.x,self.y)
        print(self.rect.center,self.collide(0,0,colliders),onfloor,(round(vel[0]),round(vel[1])))

    def collide(self,x,y,colliders):
        rect = self.rect.move(x,y)
        for obj in colliders:
            if obj.collision(rct):
                return True
        
        return False

    def collision(self,rect):
        return self.rect.colliderect(rect)

    def draw(self,root):
        root.blit(self.surf,self.rect)