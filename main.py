import pygame
import Modules.scenes as s
import sys

dis = [800,600]
root = pygame.display.set_mode(dis)
clock = pygame.time.Clock()
FPS = 60

r = pygame.Surface((50,50))
r.fill((255,0,0))

def main(args):

    dtime = 1

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    return

        s.currentScene.update(dtime)

        s.currentScene.draw(root)

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