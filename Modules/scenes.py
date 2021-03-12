from Modules.scene import scene
from Modules.button import button,startbutton,returnButton,levelButton,testButton
from Modules.img import img
from Modules.background import background
from Modules.wall import wall
from Modules.player import player
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

    loadLevel(1)
    loadLevel(2)

def loadLevel(num):
    global scenes

    data = pytmx.load_pygame(f'Assets\\maps\\level{num}.tmx')
    image = pygame.image.load(f'Assets\\maps\\level{num}.png')

    objects = []

    bg = img(image)
    bg.drawOrder = -1

    p = player(400,300)

    for obj in data.objects:
        if obj.type != None:
            pass
        else:
            objects.append(wall(list(obj.points)))


    scenes[f'level{num}'] = scene([bg,p]+objects)

loadAssets()

currentScene = scenes['Main']