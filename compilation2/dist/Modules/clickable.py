from Modules.object import object
import pygame


class clickable(object):
    prevClick = False
    time = 0

    def __init__(self,rect):
        self.rect = rect.copy()

    def update(self,dtime,objects):
        pressed = pygame.mouse.get_pressed()[0]
        mpos = pygame.mouse.get_pos()

        if self.rect.collidepoint(mpos):
            if pressed:
                if not self.prevClick:
                    if self.time > 10:
                        self.onClick(dtime,objects)
                    else:
                        self.prevClick = True
                    self.prevClick = True
                self.onHold(dtime,objects)
            else:
                if self.prevClick:
                    self.onRelease(dtime,objects)
                    self.prevClick = False
                self.onHover(dtime,objects)
        
        else:
            self.onNothing(dtime,objects)

        if self.time < 10:
            self.time += dtime

    def onClick(self,dtime,objects):pass
    def onHover(self,dtime,objects):pass
    def onHold(self,dtime,objects):pass
    def onRelease(self,dtime,objects):pass
    def onNothing(self,dtime,objects):pass

    def reset(self):
        self.time = 0

