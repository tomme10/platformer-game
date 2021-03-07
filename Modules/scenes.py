from Modules.scene import scene
from Modules.button import button
from Modules.img import img
from Modules.background import background
import pygame

r = pygame.Surface((800,50))
g = pygame.Surface((800,50))
b = pygame.Surface((800,50))
r.fill((255,0,0))
g.fill((0,255,0))
b.fill((0,0,255))

scenes = {
    'Main' : scene([img(r),background((10,10,10)),button( pygame.Rect((0,0,800,50)),r,g,b )]),
    'Secondary' : scene([background((255,255,255))])
}

currentScene = scenes['Main']