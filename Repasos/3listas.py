''' Crear una función que devuelva una lista con los números primos de 0 a 100.'''
lista= range(2,100)
def esPrimo (lista):
    for i in lista:
        if i % 2 != 0 :
            print(i)

'''– Dada una lista, imprimir los elementos en posición par.'''
lis = range(0,100)

def listarPares(lis):
    for i in range(0,len(lis),2):
        print(i)

'''– Un número es perfecto si la suma de sus divisores es igual a si mismo, ejemplo el 28. Crear una función que devuelva si un
número es perfecto.'''

def perfecto(n):
    sum=0
    for i in range(1,n):
        if n% i==n:
            sum+=i
    return sum==n

'''
[1, 2, 3] -> [(1, 1, 1), (2, 4, 8), (3, 9, 27)]'''
def tuplas (lista):
    '''
    Crear una función que recibe una lista de números y devuelve
    una lista de tuplas por cada elemento. Cada tupla tendrá el
    elemento, su cuadrado y su cubo:
    :param lista:
    :return:
    '''
    lis=[]
    for i in lista:
        lis.append((i,i**2,i**3))

    return lis



if __name__ == "__main__" :
    #esPrimo(lista)
    listarPares(lis)
    print(perfecto(22))
    list = range(1,4)
    print(tuplas(list))