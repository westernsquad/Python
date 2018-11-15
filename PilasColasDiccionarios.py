# -*- coding: utf-8 -*-
"""Copia de Untitled0.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1zZDhWoZ5_nh37fhmMlR4GWHv6qmrBlWJ
"""

#Lista de los numeros (Operandos)
# Pila de operadores, si es el primero lo guardo, si no, pues miro la prioridad del que hay y el que viene
#Si tienen misma prioridad o menos, desapilo
# Distinta prioridad dentro de la pila y fuera
# Si tengo un cierre de parentesis, tengo que desapilar
#Funcion isDigits() y Split()

def apilar(pila, elemento):
    pila.append(elemento)

def desapilar(pila):
    return pila.pop()

def cima(pila):
    return pila[-1]

def encolar(cola, elemento):
    cola.insert(0,elemento)
    
def desencolar (cola):
    return cola.pop()

def primero(cola):
    return cola[-1]

def preordenIn (operador):
    if operador == "(" :
        return 0
    elif operador == "+"  or operador == "-" :
        return 1
    elif operador == "*" or operador == "/" :
        return 2
    elif operador == "^" :
        return 3
    
def preordenOut (operador):
    if operador == "(" :
        return 5
    elif operador == "+"  or operador == "-" :
        return 1
    elif operador == "*" or operador == "/" :
        return 2
    elif operador == "^" :
        return 4
    
def postFija (lista):
    pf = []
    pila = []  
    for elemento in lista:
        if elemento.isdigit() :
            pf.append(elemento)
        else:
            if len(pila) == 0 : # Pila Vacia
                apilar(pila, elemento)
            elif elemento == ")": #Caso peculiar, si llego al cierre resuelvo. Recorro todo desapilando hasta (
                while cima(pila) != "(":
                    pf.append(desapilar(pila)) # Desapilo guardando en postfija pf 
                desapilar(pila)
            elif preordenIn(cima(pila) ) < preordenOut(elemento) : # Si es de mayor prioridad apilo sin más
                apilar(pila, elemento)
            else: 
                while len(pila) != 0 and preordenIn(cima(pila) ) >= preordenOut(elemento) : # Si es menor prioridad o igual
                    pf.append(desapilar(pila))
                apilar(pila, elemento)
            
    while len(pila) != 0 :
        pf.append(desapilar(pila))
    return pf
            
    
def solve (expresion):
    l = expresion.split()
    print(l)
    pf = postFija(l)
    print(pf)
    return print(resultado(pf))
 
def calc (a,b,o):
    if  o == "+" :
        return str(int(a) + int(b))
    elif o == "-":
        return str(int(a) - int(b))   
    elif o == "*":
        return str(int(a) * int(b)) 
    elif o == "/":
        return str(int(a) // int(b)) 
    elif o == "^":
        return str(int(a) ** int(b))   
    
def resultado (listaPF):
    pila = []
    for e in listaPF :
        if e.isdigit() :
            apilar(pila, e)
        else : 
            b = desapilar(pila)
            a = desapilar(pila)
            apilar(pila, calc(a,b,e))
    return cima(pila)
    
expresion = ' 4 - 5 ^ ( 5 - 2 ) + 9 * 7 - 24 / ( 7 - 2 ) '
solve(expresion)

#– Reimplementar la función del calculo de los 100 primeros primos haciendo uso de conjuntos.
def isprime(n,p):
  for e in p:
      if n % e ==0:
         return False;
  return True

def primos ():
  p=set()
  for e in range(2, 100):
    if isprime(e,p):
        p.add(e)
      
  return p

print(primos())
#– Crear una función que recibe un número y devuelve una lista con sus dígitos.
def digitos(n):
  l=[]
  while n:
    l.insert(0,n%10)
    n//=10
  print(l)
  
def digitos2(n):
  l=[]
  for e in str(n):
    l.append(int(e))
  print(l)

print(digitos(123456))
print(digitos2(654321))
#– Un número es cubifinito si al elevar al cubo sus dígitos y sumarlos da como resultado 1 u otro número cubifinito. Crear una función que reciba un número y devuelva si es cubifinito.
#– Implementar las funciones sobre conjunto, unión, intersección, diferencia y copia.
def union (s1,s2):
  s=set()
  for e in s1:
    s.add(e)
  for e in s2:
    s.add(e)
    
  return s

def interseccion (s1,s2):
  s=set()
  for e in s1:
    if e in s:
        return s
    else:
      s.add(e)
  for e in s2:
    if e in s:
      return s
    else:
       s.add(e)
    
  return s

def diferencia (c1,c2):
  c= set()
  for e in c1:
    if e not in c2:
      c .add(e)
      
  return c

def copy(c):
  c2 = set()
  for e in c:
    c.add(e)
  return c2


print(union((1,2,3),(4,5)))
print(interseccion((1,2,3),(4,5)))
print(diferencia((1,2,3),(4,5)))

l= digitos(11)
"""def escubifinito (n,l):
  cf = {1}
  c= set()
  
  s=0
  for e in l:
    s += e**3
  if s in cf:
    return True
  
  elif s in c:
    return False
  else :
    c.add(s)
    escubifinito()"""
    
    
#print(escubifinito (11,l))
#de la lista borramos el umero q no tiene parejas en este el 5, sumando todos los numero te quedan el q esta solo
lista=[3,5,-7,-9,-3,7,9]
def opositepair(l):
  c=set()
  for e in l:
    if e not in c:
      c.add(-e)
    else:
      c.remove(e)
  return -c.pop()


print(opositepair(lista))


#quitar numero repetido
lis=[3,3,5,5,4,4,3,3,1]
def single(l):
  c=set()
  for e in l:
    if e not in c:
      c.add(e)
    else:
      c.remove(e)
  return c.pop()
  
  
def single2(l):
  c=0
  for e in l:
     c ^= e
  return c
print(single(lis))
print(single2(lis))

#funcion q devueve una tumpla separando pares e impares

def evensplit(c1):
  e = set()
  o = set()
  for i in c1:
    if i%2 ==0:
      e.add(i)
    else:
      o.add(i)
  return e,o
c=(1,2,3,4,5)
print(evensplit(c))

import random
#ejercicios parte deDicionarios
lista=[1,2,3]
lista2=[4,5]
def cartesiano (c1,c2):
  c3 = set()
  for e in c1:
    for i in c2:
       c3.add((e,i))
        
  return c3

  
print(cartesiano(lista,lista2))

#Crear una función que devuelva el número de apariciones de cada carácter en una cadena.
def aparciones (cadena):
  c=0
  d=dict() 
  for e in cadena:
    if e not in d:
      d[e]=1
    else:
      d[e] +=1
  return d
      
#Utilizando el modulo random, crear una función que simule N tiradas de 2 dados y cuente las veces que aparece un resultado
def tiradas (n):
  d=dict(zip(list(range(2,3)),[0]*11))
  #d={2:0,3:0,4:0,5:0,6:0,7:0,8:0,9:0,10:0,11:0,12:0} 
  for e in range(n):
    d1= random.randint(1, 6)
    d2= random.randint(1, 6)
    d[d1+d2]+=1
    
  print(d)
  
tiradas(9)