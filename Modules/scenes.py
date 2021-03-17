from Modules.scene import scene,levelScene,mainScene,levelSelectScene
from Modules.button import button,startbutton,returnButton,levelButton,testButton,resetButton
from Modules.img import img
from Modules.background import background
from Modules.wall import wall
from Modules.player import player
from Modules.flag import flag
from Modules.animation import animation
from Modules.corruption import orb
import Modules.bgSound as s
from Modules.sound import sound
from Modules.bgSound import *
from Modules.portal import portal
import pygame
import pytmx

scenes = {
}
currentScene = None

level = 1

pygame.init()
rt = pygame.display.set_mode((800,600))

def changeScene(scene):
    global currentScene
    s.stopAll()
    currentScene = scene
    currentScene.reset()


# this has to be in here otherwise i would get import errors



mainMenuAnimations = [pygame.image.load(f'Assets\\startMenu\\startMenuBG{i+1}.png') for i in range(6)]
playButton = pygame.image.load('Assets\\play.png')
playHover = pygame.image.load('Assets\\playHover.png')

levelImg = pygame.image.load('Assets\\levelSelectBG.png')
returnArrow = pygame.image.load('Assets\\returnArrow.png')

resetSurf = pygame.image.load('Assets\\reset.png')


def loadAssets():
    global scenes

    buttons = [levelButton((80*i+25+80,300),i+1) for i in range(8)]

    scenes['Main'] = mainScene([animation(mainMenuAnimations,100),startbutton(playButton,(400,300),playHover),sound(wind)])
    scenes['Level Select'] = levelSelectScene([img(levelImg),returnButton(returnArrow,(50,50)),sound(wind),sound(whiteNoise,1)]+buttons)

    loadLevel(1)
    loadLevel(2)
    loadLevel(3)
    loadLevel(4,False)


def loadLevel(num,next = True):
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
        elif obj.type == 'img':
            objects.append(img(obj.image,(obj.x+obj.width//2,obj.y+obj.height//2)))
        elif obj.type == 'orb':
            objects.append(orb((obj.x,obj.y)))
        elif obj.type == 'gravPortal':
            objects.append(portal((obj.x,obj.y),obj.angle))
        elif obj.type == None:
            objects.append(wall(list(obj.points)))


    scenes[f'level{num}'] = levelScene(num,[bg,p,returnButton(returnArrow,(50,50)),resetButton(resetSurf,(800-50,50))]+objects,next)


loadAssets()

currentScene = scenes['Main']