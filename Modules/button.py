from Modules.clickable import clickable
import Modules.scenes as s

class button(clickable):

    def __init__(self,surf,pos,hovering = None,clicking = None):
        self.rect = surf.get_rect()
        self.rect.center = pos
        self.surf = surf
        self.normal = self.surf.copy()
        self.hovering = hovering.copy()
        self.clicking = clicking

    def onHold(self,objects):
        if self.clicking:
            self.surf = self.clicking.copy()

    def onHover(self,objects):
        if self.hovering:
            self.surf = self.hovering.copy()

    def onNothing(self,objects):
        self.surf = self.normal.copy()

    def onClick(self,objects):
        pass

    def draw(self,root):
        root.blit(self.surf,self.rect)

class startbutton(button):
    def onClick(self,objects):
        s.currentScene = s.scenes['Level Select']
