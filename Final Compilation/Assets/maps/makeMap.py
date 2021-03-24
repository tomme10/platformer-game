import sys
import pytmx
import pygame
from math import sin,cos,sqrt,atan2,radians
pygame.init()

root = pygame.display.set_mode((800,600))

color = (203,219,252)

def main(args):
    filename = args[1]

    surf = pygame.Surface((800,600),pygame.SRCALPHA)

    mapData = pytmx.load_pygame(filename)

    for obj in mapData.objects:
        if obj.type == None:
            xies = [obj.points[i][0] for i in range(4)]
            yies = [obj.points[i][1] for i in range(4)]
            center = (sum(xies)/len(xies),sum(yies)/len(yies))

            p = []
            for point in obj.points:
                p.append(list(point))
            
            for point in p:
                if point[0] > center[0]:
                    point[0] -= 5
                else:
                    point[0] += 5
                
                if point[1] > center[1]:
                    point[1] -= 4
                else:
                    point[1] += 3

            pygame.draw.polygon(surf,color,p,9)

        if obj.type == 'gravPortal':
            pts = obj.x,obj.y
            pts2 = list(pts)
            pts2[0] += sin(radians(obj.angle+90))*100
            pts2[1] += cos(radians(obj.angle+90))*100
            pygame.draw.line(surf,(255,0,0),pts,pts2,3) 
            

    pygame.image.save(surf,'out.png')



if __name__ == '__main__':
    try:
        main(sys.argv)
    except Exception as e:
        pygame.quit()
        raise e
