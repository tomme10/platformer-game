from Modules.scene import scene
from Modules.button import button,startbutton,returnButton,levelButton,testButton
from Modules.img import img
from Modules.background import background
from Modules.wall import wall
from Modules.player import player
from Modules.flag import flag
import pygame
import pytmx

scenes = {
}
currentScene = None

pygame.init()
rt = pygame.display.set_mode((800,600))


# this has to be in here otherwise i would get import errors
class levelScene(scene):
    def __init__(self,level,objects = [],next = True):
        super().__init__(objects)
        self.level = level
        self.next = next

        self.blackOut = pygame.Surface((800,1000))
        pygame.draw.rect(self.blackOut,(0,0,255),(0,0,800,600),10)
        self.blackOuty = 0
        self.ended = False
        self.time = 1


    def update(self,dtime):
        global scenes,currentScene

        if not self.ended:        
            super().update(dtime)
            for obj in self.objects:
                if type(obj).__name__ == 'flag':
                    if obj.touching:
                        self.ended = True

        else:
            super().update(min(20,10/dtime))
            self.time += dtime
            self.blackOuty = (800/1000)*self.time

            if self.time > 1000:
                if self.next:
                    currentScene = scenes[f'level{self.level+1}']
                else:
                    currentScene = scenes[f'Main']


    def draw(self,root):
        super().draw(root)
        if self.ended:
            root.blit(self.blackOut,(0,self.blackOuty-1000))





def loadAssets():
    global scenes
    mainImg = pygame.image.load('Assets\\startMenuBG.png')
    playButton = pygame.image.load('Assets\\play.png')
    playHover = pygame.image.load('Assets\\playHover.png')

    levelImg = pygame.image.load('Assets\\levelSelectBG.png')
    returnArrow = pygame.image.load('Assets\\returnArrow.png')
    levelicons = pygame.image.load('Assets\\levelicons.png')
    levelNormal = []
    levelHover = []

    for i in range(8):
        surf = pygame.Surface((75,75))
        surf.blit(levelicons,(-i*75,0))
        levelNormal.append(surf.copy())
        surf.blit(levelicons,(-i*75,-75))
        levelHover.append(surf.copy())

    buttons = [levelButton(levelNormal[i],(80*i+25+80,300),i+1,levelHover[i]) for i in range(8)]

    scenes['Main'] = scene([img(mainImg),startbutton(playButton,(400,300),playHover)])
    scenes['Level Select'] = scene([img(levelImg),returnButton(returnArrow,(50,50))]+buttons)

    loadLevel(1)
    loadLevel(2)
    loadLevel(3)

def loadLevel(num):
    global scenes

    data = pytmx.load_pygame(f'Assets\\maps\\level{num}.tmx')
    image = pygame.image.load(f'Assets\\maps\\level{num}.png')

    objects = []

    bg = img(image)
    bg.drawOrder = -1

    p = player(400,300)

    for obj in data.objects:
        if obj.type == 'flag':
            objects.append(flag(obj.x,obj.y,obj.rotation))
            print('flag')
        elif obj.type == 'img':
            objects.append(img(obj.image,(obj.x+obj.width//2,obj.y+obj.height//2)))
        elif obj.type == None:
            objects.append(wall(list(obj.points)))


    scenes[f'level{num}'] = levelScene(num,[bg,p]+objects)

loadAssets()

currentScene = scenes['Main']