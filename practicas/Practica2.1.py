
import numpy as np
import collections

Point = collections.namedtuple("Point", ["x", "y"])
Recta = collections.namedtuple('Recta', ['uno', 'dos'])

Triangulo = collections.namedtuple('Triangulo', ['v0', 'v1', 'v2'])
Cuadrilatero= collections.namedtuple('Cuadrilaterp',['t1','t2'])



def borde (recta, punto):
    return  (punto.x - recta.uno.x) * (recta.dos.y - recta.uno.y) - (punto.y - recta.uno.y) * (recta.dos.x - recta.uno.x)


def inTriangle (trinagulo,punto):
    return (borde(trinagulo.v0,punto) <= 0) and (borde(trinagulo.v1,punto) <= 0) and (borde(trinagulo.v2,punto) <= 0)

def rasterice(screen,t,value):
    f,c=screen.shape
    for i in range(f):
        for j in range(c):
            p=Point(j, i)
            if inTriangle(t,p):
                screen[i][j]=value
#*******************************************poligono
def poligono (p0,p1,p2,p3):
    t1=Triangulo(p0,p1,p2)
    t2=Triangulo(p2,p3,p0)
    c=Cuadrilatero(t1,t2)
    return t1,t2

def rastericeP(screen,t1,t2,value):
    f,c=screen.shape
    for i in range(f):
        for j in range(c):
            p=Point(j, i)
            if inTriangle(t1,p) or inTriangle(t2,p):
                screen[i][j]=value


if __name__ == "__main__":
    screen = np.zeros((10,10))
    print (screen)

    prueba=Point(7, 4 )
    p = Point(2, 4)
    q = Point(5, 3)
    s = Point(5, 6)
    l = Point(2, 6)


    r =Recta(p, q)
    r1 =Recta(q, s)
    r2 =Recta(s, p)
    r11=Recta(s,l)
    r22=Recta(l,p)
    r33=Recta(p,s)
    t= Triangulo(r,r1,r2)
    t2= Triangulo(r11,r22,r33)
    #pol=poligono(p,q,s,l)


    #tt= Triangulo(p,q,s)
    print (borde(r,prueba))
    print (borde(r1,prueba))
    print (borde(r2,prueba))
    print(inTriangle(t,prueba))
    rasterice(screen,t,4)
    print (screen)
    #rastericeP(screen, t,t2,4)
    rastericeP(screen, t,t2, 4)
    print (screen)





