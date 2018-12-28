# coding=utf-8
import math
# Crear una función que dada una altura, pinte un rombo.
def rombo (a):
    '''
    funcion que imprime por pantalla un rambo
    :param a:Altura de la mitad del romb
    :return:
    '''
    for i in range (a):
        print(' ' * (a - i) + '*' * (2 * i + 1))

    for i in range(a - 2, -1, -1):
        print(' ' * (a - i) + '*' * (2 * i + 1))
# Crear una función que devuelva el área de un rectángulo.
def areaRectangulo(b, a):
    print('El area del rectangulo con base = ' + str(b) + 'y altura = '+ str(a) + 'es =' + str(b*a))
# Crear una función que devuelva el perímetro de una circunferencia (utilizando math).
def perimetroCircunferencia (r):
    perimetro= 2* math.pi *r
    print('El perimetro de la circunferencia de radio'+str(r)+'es de ='+str(perimetro))

# Crear una función que resuelve una ecuación de segundo grado recibiendo a, b, c.
def segundoGrado (a, b , c):
    t = (((-b) + math.sqrt((b ** 2 + (4 * a * c) / 2 * a))), ((-b) - math.sqrt((b ** 2 + (4 * a * c) / 2 * a))))
    for i in t:
        print('La ecuacion de segundo grado es =' + str(i))

# Crear una función que calcule el factorial de n
def factorial (n):
    f=1
    for i in range(n+1):
        if i != 0 :
            f= f*i
        else:
            continue

    print('el factorial de 5 es  ='+ str(f))
if __name__ == "__main__" :
    rombo(3)
    areaRectangulo(5,2)
    perimetroCircunferencia(3)
    segundoGrado(1,2,3)
    factorial(5)