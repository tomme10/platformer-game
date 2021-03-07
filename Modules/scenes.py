from Modules.scene import scene
from Modules.button import button,startbutton
from Modules.img import img
from Modules.background import background
import pygame

mainImg = pygame.image.load('Assets\\startMenuBG.png')
playButton = pygame.image.load('Assets\\play.png')
playHover = pygame.image.load('Assets\\playHover.png')

scenes = {
    'Main' : scene([img(mainImg),startbutton(playButton,(400,300),playHover)]),
    'Level Select' : scene([background((255,255,255))])
}

currentScene = scenes['Main']