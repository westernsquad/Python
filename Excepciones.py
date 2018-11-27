'''
    La función input muestra un mensaje que se pasa por parámetro
y espera a que el usuario introduzca un dato por teclado. Crear
una función que se asegure que el usuario introduce un entero
(avisando cada vez que se equivoque).
'''

def inputt():
    while True:
        try:
            x = int(input("Por favor ingrese un número: "))
            break
        except ValueError:
            print("Oops! No era válido. Intente nuevamente...")
inputt()


def get (d,k,v):
    try:
        return d[k]
    except KeyError :
        return v

print (get(({1:"hola"}),1,2))
