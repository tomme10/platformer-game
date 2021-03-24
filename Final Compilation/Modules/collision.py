
createAxis = lambda p1,p2:[p2[1]-p1[1],p1[0]-p2[0]]

def rect2rect(a,b):

    axes = []

    for i in range(4):
        axes.append(createAxis(a[i%len(a)],a[ (i+1)%len(a) ]))
    for i in range(4):
        axes.append(createAxis(b[i%len(b)],b[ (i+1)%len(b) ]))

    collision = True

    for axis in axes:

        projected = 0

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
            collision = False
            break

    return collision