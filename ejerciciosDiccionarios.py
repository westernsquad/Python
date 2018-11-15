""""Pagina 50 de las diapositivas
Reimplementar las funciones que cuentan caracteres y
palabras.
 Crear una función que devuelva el diccionario inverso.
 Crear una función que gestione una agenda, permitirá agregar números de teléfono a personas.
 Crear una función que escribe una cadena en Morse.
 Crear la función inversa, de una cadena en Morse devuelve la traducción."""

#1
def cuentan (c):
   #Reimplementar las funciones que cuentan caracteres y palabras.
    d=dict()
    palabras = c.split()
   #Cuenta y crea caracteres en el diccionario
    for e in c:
        if e not in d :
            d[e]=1
        else:
            d[e]+=+1
   #Cuenta y crea caracteres en el diccionario
   # Cuenta y crea Palabras en el diccionario
    for j in palabras:
        if j not in d:
            d[j] = 1
        else:
            d[j] += +1

    print(palabras)
    print(d)
    #Cuenta y crea Palabras en el diccionario
cuentan('hola que tal mariano')

#2
'''Funcion que devuelve la inversa de un diccionario'''
agenda={'Luis' : 689332211, 'Maria': 753951456, 'Julio' : 147852654}
morse = {'A': '.-', 'B': "-...", 'C': '-.-.', 'D': '-..', 'E': '.', 'F': '..-.', 'G': '--', 'H': '....', 'I': '..',
         'J': '.---', 'K': '-.-', 'L': '.-..', 'M': '--', 'N': '-.', 'Ñ': '--.--', 'O': '---', 'p': '.--.', 'Q': '--.-',
         'R': '.-.', 'S': '...', 'T': '-', 'U': '..--', 'V': '...-', 'W': '.--', 'X': '-..-', 'Y': '-.--', 'Z': '--..',
         '0': '-----', '1': '.----', '2': '..---', '3': ':...--', '4': '....-', '5': '.....', '6': '-....',
         '7': '--...', '8': '---..', '9': '----.', '.': '.-.-.-', ',': '-.-.--', '?': '..--..', '"': '.-..-.',
         '!': '--..--'}


def inverso1 (dic):
    k=dic.keys()
    v=dic.values()
    d=dict(zip(v,k))
    print(d)

def inverso2 (dic):
    k = dic.items()
    d={}
    lista=[]
    for e in k:
        lista.append(e)
    lista=list(reversed(lista))
    for k, v in lista:#se pueden acceder asi a los elementos de la tupla
        d[k]=v

    print(d)

inverso1(morse)
inverso2(agenda)
#3

def agenda (persona,telefono):
    '''Recive dos parametro, nombre y un telefono , y se podran anadir a la agenda'''
    agenda = {'Luis': 689332211, 'Maria': 753951456, 'Julio': 147852654}
    d=dict()
    for k in agenda:
        if persona == k:
            d[k]=telefono
        else:
            d[persona]=telefono
    agenda.update(d)
    print(agenda)

agenda('Raul',698352456)

#4
def morse (cadena):#preguntar por que no me guarda los espacios¿Tendre q meter cada letra una a una sin  usar split?

    traduccido=[]
    morse = {' ':' ','.-': 'A', '-...': 'B', '-.-.': 'C', '-..': 'D', '.': 'E', '..-.': 'F', '--': 'M', '....': 'H', '..': 'I', '.---': 'J', '-.-': 'K', '.-..': 'L', '-.': 'N', '--.--': 'Ñ', '---': 'O', '.--.': 'p', '--.-': 'Q', '.-.': 'R', '...': 'S', '-': 'T', '..--': 'U', '...-': 'V', '.--': 'W', '-..-': 'X', '-.--': 'Y', '--..': 'Z', '-----': '0', '.----': '1', '..---': '2', ':...--': '3', '....-': '4', '.....': '5', '-....': '6', '--...': '7', '---..': '8', '----.': '9', '.-.-.-': '.', '-.-.--': ',', '..--..': '?', '.-..-.': '"', '--..--': '!'}
    #letras = ' '.join(cadena.split())
    palabras= cadena.split()
    print(palabras)
    for e in palabras:
        letra=e.split()
        for j in letra :
            traduccido.append(morse.get(j))
    cadena1= ''.join(traduccido)
    print(cadena1)
    print(traduccido)
morse('.... --- .-.. .-   -.-. .- .-. .-   -.-. --- .-.. .- ')
