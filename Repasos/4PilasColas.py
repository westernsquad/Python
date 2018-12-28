

'''***************PILAS********************'''
def apilar(pila, elemento):
    pila.append(elemento)

def desapilar(pila):
    pila.pop()

def cima(pila):
    cima=pila.pop()
    apilar(pila,cima)
    return cima

'''*******************COLAS*************'''
def encolar(cola, elemento):
    cola.insert(0,elemento)
def desencolar(cola):
    cola.pop()
def primero(cola):
    return cola [-1]

'''– Implementa un programa que devuelva si en una cadena que
recibe de entrada, los paréntesis que en ella aparecen están
balanceados'''

def balanceado (cadena):
    l=[]
    for i in range (0,len(cadena)):
        if i == '(':
            apilar(l,i)
        elif i == ')':
            desapilar(pila)
    if len(l)==0:
        print('La cadena esta balanceada')
    else:
        print('La cadena no esta balanceada')
if __name__ == "__main__" :
    pila =[1,2,3]
   # desapilar(pila)
    print(pila)
    print(cima(pila))
    print(pila)

    cola=[1,2,3]
    desencolar(cola)
    print(cola)
    print(primero(cola))

    cadena = '(si esta balanceada (()))'
    balanceado(cadena)