import numpy as np

def createAxis(p1,p2):
    return [p2[1]-p1[1],p1[0]-p2[0]]

def rect2rect(a,b):

    axes = [createAxis(a[0],a[1]),createAxis(a[1],a[2]),createAxis(b[0],b[1]),createAxis(b[1],b[2])]

    for axis in axes:

        mina = None
        minb = None
        maxa = None
        maxb = None

        for point in a:
            projected = point[0]*axis[0]+point[1]*axis[1]
            if mina == None or projected < mina:
                mina = projected
            if maxa == None or projected > maxa:
                maxa = projected

        for point in b:
            projected = point[0]*axis[0]+point[1]*axis[1]
            if minb == None or projected < minb:
                minb = projected
            if maxb == None or projected > maxb:
                maxb = projected

        if maxa < minb or maxb < mina:
            return False

    return True