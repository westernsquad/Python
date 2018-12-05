
import numpy as np
import collections

Point = collections.namedtuple("Point",["x","y"])
Recta = collections.namedtuple('Recta',[ 'uno' , 'dos'])

Rectangle = collections.namedtuple("Rectangle",["min","max"])
Triangulo = collections.namedtuple('Triangulo',['iz','cen','der'])

def borde (recta, punto):
    return (punto.x - recta.uno.x) * (recta.dos.y - recta.uno.y) - (punto.y - recta.uno.y) * (recta.dos.x - recta.uno.x)


def inTriangle (trinagulo,punto):
    #return (borde(trinagulo.iz,punto) >= 0) and (borde(trinagulo.cen,punto) >= 0) and (borde(trinagulo.der,punto) >= 0)
    e=borde(trinagulo.iz,punto)
    e2=borde(trinagulo.cen,punto)
    e3=borde(trinagulo.der,punto)
    print('primero'+ str(e) )
    print('segundoo' + str(e2) )
    print('terceroo' + str(e3) )

screen = np.zeros((10,10))
print (screen)

'''changepixel(screen,2,3,4)
print(screen)

clearscreen(screen)
print (screen)'''

prueba=Point(0,0)
p = Point(0, 0)
q = Point(3,0)
s = Point(3,3)


r =Recta(p, q)
r1 =Recta(q, s)
r2 =Recta(s, p)
t= Triangulo(r,r1,r2)
borde(r2,prueba)
print(inTriangle(t,prueba))




