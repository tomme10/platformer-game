from Modules.scene import scene
from Modules.button import button,startbutton,returnButton
from Modules.img import img
from Modules.background import background
import pygame

mainImg = pygame.image.load('Assets\\startMenuBG.png')
playButton = pygame.image.load('Assets\\play.png')
playHover = pygame.image.load('Assets\\playHover.png')

levelImg = pygame.image.load('Assets\\levelSelectBG.png')

returnArrow = pygame.image.load('Assets\\returnArrow.png')

scenes = {
    'Main' : scene([img(mainImg),startbutton(playButton,(400,300),playHover)]),
    'Level Select' : scene([img(levelImg),returnButton(returnArrow,(50,50))])
}

currentScene = scenes['Main']