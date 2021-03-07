from Modules.clickable import clickable
import Modules.scenes as s

class button(clickable):

    def __init__(self,rect,surf,hovering = None,clicking = None):
        self.rect = rect
        self.surf = surf
        self.normal = self.surf.copy()
        self.hovering = hovering.copy()
        self.clicking = clicking

    def onHold(self,objects):
        self.surf = self.clicking.copy()

    def onHover(self,objects):
        self.surf = self.hovering.copy()

    def onNothing(self,objects):
        self.surf = self.normal.copy()

    def onClick(self,objects):
        s.currentScene = s.scenes['Secondary']

    def draw(self,root):
        root.blit(self.surf,self.rect)
