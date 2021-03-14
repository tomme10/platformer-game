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
        super().__init__(objects)
        self.level = level
        self.next = next

        self.blackOut = pygame.image.load('Assets\\transition.png')
        self.blackOuty = 600
        self.ended = False
        self.endTime = 1

        self.started = True
        self.startTime = 1



    def update(self,dtime):
        global scenes,currentScene

        if not self.ended and not self.started:        
            super().update(dtime)
            for obj in self.objects:
                if type(obj).__name__ == 'flag':
                    if obj.touching:
                        self.ended = True

        elif self.ended:
            super().update(0.1)
            self.endTime += dtime
            self.blackOuty = (700/1500)*self.endTime

            if self.endTime > 1500:
                if self.next:
                    changeScene(scenes[f'level{self.level+1}'])
                else:
                    changeScene(scenes[f'Main'])

        elif self.started:
            super().update(0.1)
            self.startTime += dtime
            self.blackOuty = 700-(700/1500)*self.startTime

            if self.startTime > 1500:
                self.started = False
                super().reset()


    def draw(self,root):
        super().draw(root)
        if self.ended or self.started:
            root.blit(self.blackOut,(0,self.blackOuty-1000))

    def reset(self):
        super().reset()
        self.started = True
        self.ended = False
        self.endTime = 1
        self.startTime = 1 
