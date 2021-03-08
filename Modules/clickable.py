from Modules.object import object
import pygame


class clickable(object):
    prevClick = True

    def __init__(self,rect):
        self.rect = rect.copy()

    def update(self,dtime,objects):
        pressed = pygame.mouse.get_pressed()[0]
        mpos = pygame.mouse.get_pos()

        if self.rect.collidepoint(mpos):
            if pressed:
                if not self.prevClick:
                    self.onClick(objects)
                    self.prevClick = True
                self.onHold(objects)
            else:
                if self.prevClick:
                    self.onRelease(objects)
                    self.prevClick = False
                self.onHover(objects)
        
        else:
            self.onNothing(objects)

    def onClick(self,objects):pass
    def onHover(self,objects):pass
    def onHold(self,objects):pass
    def onRelease(self,objects):pass
    def onNothing(self,objects):pass

