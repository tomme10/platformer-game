from Modules.clickable import clickable
import Modules.scenes as s
import pygame

class button(clickable):

    def __init__(self,surf,pos,hovering = None,clicking = None):
        self.rect = surf.get_rect()
        self.rect.center = pos
        self.surf = surf
        self.normal = self.surf.copy()
        self.hovering = hovering
        self.clicking = clicking

    def onHold(self,dtime,objects):
        if self.clicking:
            self.surf = self.clicking.copy()

    def onHover(self,dtime,objects):
        if self.hovering:
            self.surf = self.hovering.copy()

    def onNothing(self,dtime,bjects):
        self.surf = self.normal.copy()

    def onClick(self,dtime,objects):
        pass

    def draw(self,root):
        root.blit(self.surf,self.rect)

class startbutton(button):
    
    clicked = False

    def onClick(self,dtime,objects):
        self.clicked = True

    def reset(self):
        self.clicked = False

class returnButton(button):
    def onClick(self,dtime,objects):
        s.changeScene(s.scenes['Main'])

class levelButton(button):

    clicked = False
    hover = False

    def __init__(self,pos,level):
        self.level = level
        self.locked =  self.level > s.level
        spriteSheet = pygame.image.load('Assets\\levelicons.png')

        self.normal = pygame.Surface((75,75))
        self.normal.blit(spriteSheet,(-75*(level-1),0))

        self.hoverFrames = []
        self.index = 0
        for i in range(4):
            surf = pygame.Surface((75,75))
            surf.blit(spriteSheet,(-75*(level-1),-(75+i*75)))
            self.hoverFrames.append(surf.copy())
        self.animTime = 0

        self.lockedSurf = pygame.Surface((75,75))
        self.lockedSurf.blit(spriteSheet,(-75*(level-1),-75*5))
        
        if self.locked:
            self.surf = self.lockedSurf.copy()
        else:
            self.surf = self.normal.copy()

        self.rect = self.surf.get_rect()
        self.rect.center = pos

    def onHold(self,dtime,objects):
        pass

    def onNothing(self,dtime,objects):
        if not self.locked:
            self.surf = self.normal.copy()
            self.hover = False

    def onHover(self,dtime,objects):
        if not self.locked:
            self.surf = self.hoverFrames[self.index].copy()
            self.animTime += dtime

            if self.animTime > 100:
                self.animTime = 0
                self.index += 1
                self.index %= len(self.hoverFrames)

            self.hover = True

    def onClick(self,dtime,objects):
        if not self.locked:
            self.clicked = True
            #s.changeScene(s.scenes[f'level{self.level}'])

    def reset(self):
        self.clicked = False
        self.locked =  self.level > s.level
        self.hover = False

class testButton(button):

    def onClick(self,dtime,objects):
        print('click')

    def onRelease(self,dtime,objects):
        print('release')

class resetButton(button):

    clicked = False

    def onClick(self,dtime,objects):
        self.clicked = True

    def reset(self):
        self.clicked = False