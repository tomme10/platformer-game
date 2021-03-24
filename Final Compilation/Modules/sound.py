from Modules.object import object
import Modules.bgSound as s
import pygame

class sound(object):
    def __init__(self,sound,channel = 0,volume = 1):
        self.sound = sound
        self.playing = False
        self.channel = channel
        self.volume = volume

        #s.play(self.sound,self.channel,loops = -1)
        #s.channels[self.channel].set_volume(volume)

    def reset(self):
        s.play(self.sound,self.channel,loops = -1)
        s.channels[self.channel].set_volume(self.volume)

    def fade(self):
        s.fade(self.channel,1000)
