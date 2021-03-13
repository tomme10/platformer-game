import pygame
import Modules.scenes as s
import sys

pygame.init()

dis = [800,600]
root = pygame.display.set_mode(dis)
clock = pygame.time.Clock()
FPS = 60

r = pygame.Surface((50,50))
r.fill((255,0,0))

font = pygame.font.SysFont('SansSherif', 18)

def main(args):

    fps = 0
    fpsShown = False

    dtime = 1

    while True:
        fps = font.render(str(fps),True,(255,255,255))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    return
                elif event.key == pygame.K_p:
                    fpsShown = not fpsShown
           
        s.currentScene.update(dtime)

        s.currentScene.draw(root)
        root.blit(fps,(0,0))

        pygame.display.update()
        dtime = clock.tick(FPS)
        fps = round(1000/dtime,1)

if __name__ == '__main__':
    try:
        main(sys.argv)
    except Exception as e:
        pygame.quit()
        raise e

    pygame.quit()
    sys.exit()