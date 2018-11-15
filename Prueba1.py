# coding=utf-8
#Area de un rectangulo

a = 1
b = 3
area = b*a
print('El area del rectangulo es: ',area)

#perimetro de una circunferencia
r=5
perimetro = (2 * 3.1416)*r
print('El perimetro de la circunferencia es: ',perimetro)

#anno bisiesto

a=2004
if ((a % 4== 0) and not (a % 100 == 0) or (a % 400 ==0)) :
    print("Es un año bisiesto", a)
else:
    print ("No es un ano bisiesto", a)

#dibujar un triangulo de asteriscos
n = 4

for i in range(n):
    print(" " * (n - i) + "*" * (2 * i + 1))
print("----------------------------")
n = 4

for i in range(n-1,-1,-1):
    print(" " * (n - i) + "*" * (2 * i + 1))

#rombo
n = 4
for i in range(n):
    print(" " * (n - i) + "*" * (2 * i + 1))
for i in range(n-2,-1,-1):
    print(" " * (n - i) + "*" * (2 * i + 1))

#Funciones

def imprime(parametro):
    print(parametro)

imprime(input("Introduce algo"))