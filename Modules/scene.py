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