import pygame
from Modules.object import object


class animation(object):
    time = 0

    def __init__(self,frames,interval = 100,center = (400,300)):
        self.frames = frames
        self.interval = interval
        self.index = 0
        self.center = center

    def update(self,dtime,objects):
        self.time += dtime

        if self.time > self.interval:
            self.time = 0
            self.index += 1
            self.index %= len(self.frames)

    def draw(self,root):
        frame = self.frames[self.index]
        root.blit(frame,(self.center[0]-frame.get_width()//2,self.center[1]-frame.get_height()//2))