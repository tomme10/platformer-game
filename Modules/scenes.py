from Modules.scene import scene
from Modules.button import button,startbutton,returnButton,levelButton
from Modules.img import img
from Modules.background import background
import pygame
import pytmx

scenes = {
}

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

    scenes['level1'] = scene([background((100,100,100))])

def loadLevel(num):
    global scenes

    data = pytmx.load_pygame('Assets\\maps\\level1.tmx')

    rects = []

    preRender = pygame.Surface((800,600))
    preRender.fill((0,0,0))
    postProcessing = pygame.Surface((800,600))
    postProcessing.fill((0,0,0))

    for obj in data.objects():
        if obj.type != '':
            pass
        else:
            pygame.draw.rect(preRender,(95,205,228),(obj.x,obj.y,obj.w,obj.h),5)
            rects.append(pygame.Rect(obj.x,obj.y,obj.w,obj.h))

    for x in range(800):
        for y in range(600):
            

    
            


loadAssets()

currentScene = scenes['Main']