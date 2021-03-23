import pygame
import Modules.scenes as s
import Modules.bgSound as sound


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
        super().__init__(objects)
        self.level = level
        self.next = next

        self.ended = False
        self.endTime = 1

        self.fadeOut = pygame.Surface((800,600))
        self.fadeOut.fill((0,0,0))
        self.fadeOut.set_alpha(0)
        self.started = True
        self.startTime = 1        


    def update(self,dtime):
        global scenes,currentScene

        if s.level < self.level:
            s.level += 1

        if not self.ended and not self.started:        
            super().update(dtime)
            for obj in self.objects:
                if type(obj).__name__ == 'flag':
                    if obj.touching:
                        self.ended = True

                if type(obj).__name__ == 'resetButton':
                    if obj.clicked:
                        self.reset()

        elif self.ended:
            super().update(0.001)
            self.endTime += dtime
            self.fadeOut.set_alpha((255/1500)*self.endTime)

            if self.endTime > 1500:
                if self.next:
                    s.changeScene(s.scenes[f'level{self.level+1}'])
                else:
                    s.changeScene(s.scenes[f'Main'])

        elif self.started:
            super().update(dtime)
            self.startTime += dtime
            self.fadeOut.set_alpha(255-(255/750)*self.startTime)

            if self.startTime > 750:
                self.started = False


    def draw(self,root):
        super().draw(root)
        if self.started or self.ended:
            root.blit(self.fadeOut,(0,0))

    def reset(self):
        super().reset()
        self.started = True
        self.ended = False
        self.endTime = 1
        self.startTime = 1 
        sound.play(sound.pinkNoise,1,-1)


class mainScene(scene):

    def __init__(self,objects):
        super().__init__(objects)
        self.ended = False

        self.blackout = pygame.Surface((800,600))
        self.blackout.fill((0,0,0))
        self.blackout.set_alpha(0)

        self.time = 0

    def update(self,dtime):

        if not self.ended:
            super().update(dtime)
            for obj in self.objects:
                if type(obj).__name__ == 'startbutton':
                    if obj.clicked:
                        self.ended = True

        else:
            super().update(dtime)
            if self.time < 1000:
                self.time += dtime
                self.blackout.set_alpha((255/1000)*self.time)
            else:
                s.changeScene(s.scenes['Level Select'])

    def draw(self,root):
        super().draw(root)
        if self.ended:
            root.blit(self.blackout,(0,0))

    def reset(self):
        super().reset()
        self.ended = False
        self.time = 0


class levelSelectScene(scene):
    
    started = True
    ended = False
    startTime = 0
    endTime = 0

    def __init__(self,objects):
        super().__init__(objects)

        self.blackOut = pygame.Surface((800,600))
        self.blackOut.fill((0,0,0))
        self.blackOut.set_alpha(0)

        self.level = 0

        self.pinkNoise = False

    def update(self,dtime):

        super().update(dtime)
        
        self.pinkNoise = False
        for obj in self.objects:
            if type(obj).__name__ == 'levelButton':
                if obj.clicked:
                    self.ended = True
                    self.level = obj.level

                elif obj.hover:
                    self.pinkNoise = True

        if self.started:
            self.startTime += dtime

            self.blackOut.set_alpha(255-(255/1000)*self.startTime)

            if self.startTime > 1000:
                self.started = False

        elif self.ended:
            self.endTime += dtime

            self.blackOut.set_alpha((255/1000)*self.endTime)

            if self.endTime > 1000:
                s.changeScene(s.scenes[f'level{self.level}'])

        if self.pinkNoise:
            if not sound.channels[1].get_busy():
                sound.play(sound.pinkNoise, 1, loops = -1)
        else:
            sound.stop(1)

    def reset(self):
        super().reset()
        self.started = True
        self.ended = False
        self.endTime = 0
        self.startTime = 0
        self.level = 0
        self.blackOut.set_alpha(0)

    def draw(self,root):
        super().draw(root)
        root.blit(self.blackOut,(0,0))
            