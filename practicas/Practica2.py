'''Rasterizador'''
import numpy as np
import collections
def clearscreen(screen):
    return screen.fill(0)

def changepixel(imagen, fila, columna , valor):
    '''f,c,v es....'''
    imagen[fila][columna] = valor


Point = collections.namedtuple("Point",["x","y"])
Rectangle = collections.namedtuple("Rectangle",["min","max"])

def inRectangle (r,x,y):

    return r.min.x <= x <= r.max.x and r.min.y <= y <= r.max.y

def rasterice(screen,rect,value):
    f,c=screen.shape
    for i in range(f):
        for j in range(c):
            if inRectangle(rect,j,i):
                screen[i][j]=value





screen = np.zeros((10,10))
print (screen)

'''changepixel(screen,2,3,4)
print(screen)

clearscreen(screen)
print (screen)'''

p = Point(0, 0)
q = Point(2,3)
r = Rectangle(p, q)
print (p)
print (p[0])
print (p.x)

print (r)
print (r[0][0])
print (r.min)

rasterice(screen,r,2)
print (screen)
