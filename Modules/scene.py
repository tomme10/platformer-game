import pygame


class scene:
    objects = []

    def __init__(self,objects = []):
        self.objects = objects

    def update(self,dtime):
        for obj in sorted(self.objects,key = lambda obj:obj.updateOrder):
            obj.update(dtime,self.objects)

    def draw(self,root):
        for obj in sorted(self.objects,key = lambda obj:obj.drawOrder):
            obj.draw(root)

    def reset(self):
        for obj in self.objects:
            obj.reset()


class levelScene(scene):
    def __init__(self,level,objects = [],next = True):
        super().__init__(self,objects)
        self.level = level
        self.next = next

    def update(self,dtime):
        super().update(dtime)
        for obj in self.objects:
            if type(obj).__name__ == 'flag' and obj.touching = True:
                if self.next:
                    currentScene = scenes[f'level{self.level+1}']
                else:
                    currentScene = scenes[f'main']
