from Modules.object import object
import pygame


class clickable(object):
    def __init__(self,rect):
        self.rect = rect.copy()

    def update(self,dtime,objects):
        pressed = pygame.mouse.get_pressed()[0]
        mpos = pygame.mouse.get_pos()

        if self.rect.collidepoint(mpos):
            if pressed:
                self.onClick(objects)
            else:
                self.onHover(objects)

    def onClick(self,objects):pass
    def onHover(self,objects):pass

