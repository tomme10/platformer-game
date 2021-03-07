import pygame
from Modules.scene import scene
from Modules.img import img
from Modules.background import background
import sys

dis = [800,600]
root = pygame.display.set_mode(dis)
clock = pygame.time.Clock()
FPS = 60

r = pygame.Surface((50,50))
r.fill((255,0,0))
scenes = {'Main':scene([img(r),background((0,0,0))])}

currentScene = scenes['Main']

def main(args):

    dtime = 0

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    return

        currentScene.update(dtime)

        currentScene.draw(root)

        pygame.display.update()
        dtime = clock.tick(FPS)

if __name__ == '__main__':
    try:
        main(sys.argv)
    except Exception as e:
        pygame.quit()
        raise e

    pygame.quit()
    sys.exit()