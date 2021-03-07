from Modules.object import object

class background(object):
    drawOrder = -1000
    
    def __init__(self,color = (0,0,0)):
        self.color = color

    def draw(self,root):
        root.fill(self.color)
