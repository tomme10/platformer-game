from Modules.object import object
import Modules.bgSound as s

class sound(object):
    def __init__(self,sound,channel = 0):
        self.sound = sound
        self.playing = False
        self.channel = channel

        s.play(self.sound,self.channel,loops = -1)

    def reset(self):
        s.play(self.sound,self.channel,loops = -1)

    def fade(self):
        s.fade(self.channel,1000)
