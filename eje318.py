# coding=utf-8
import math
#- Crear una función que dada una altura, pinte un rombo
def rombo(altura):
    for i in range(altura):
        print(" " * (altura - i) + "*" * (2 * i + 1))
    for i in range(altura - 2, -1, -1):
        print(" " * (altura - i) + "*" * (2 * i + 1))

rombo(input("Introduzca una altura: "))
#– Crear una función que devuelva el área de un rectángulo.
def area (base,altura):
    areaaux=base*altura
    print("El area del rectangulo es: ",areaaux)

area(input("Introduzca una base: "), input("Introduzca una altura: "))
#– Crear una función que devuelva el perímetro de una circunferencia (utilizando math).
def perimetro (radio):
    print("El perimetro es: ",2*math.pi*radio)

perimetro(2)
#– Crear una función que resuelve una ecuación de segundo grado recibiendo a, b, c.
def grado(a,b,c):
    print("La funcion de segundo grado es: ",(-b)+ math.sqrt((b**2+(4*a*c)/2*a)))

grado(1 ,1 ,1)
#– Crear una función que calcule el factorial de n.
#math.factorial(numero)

#hacer una funcion que te devuleva una tupla con las dos soluciones de la ecuacion de segundo grado.

def grado(a,b,c):
    t=(((-b)+ math.sqrt((b**2+(4*a*c)/2*a))),((-b)- math.sqrt((b**2+(4*a*c)/2*a))))
    for i in t:
        print("La funcion de segundo grado es: ", i)
grado(1,1,1)


#lista de primos hoja 36
#lista de primos
lista=range(2,100)
def primos (lista):
    for i in lista:
        if i % 2 != 0:
            print i

#lista de posicion pares

def pares (lista):
    for i in range(0,len(lista),2):
        print(lista[i])
pares(list(range(10)))

def perfecto(n):
    sum=0
    for i in range(1,n):
        if n% i==n:
            sum+=i
    return sum==n

def list2tupla(lista):
    l=[]
    for e in lista:
        t=(e,e**2,e**3)
        l.append(t)
    return l

print (primos(lista))
print(perfecto(25))
print(list2tupla(primos()))


