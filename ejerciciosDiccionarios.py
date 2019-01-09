
'''OrederedDict: diccionarios que conservan el orden de inserción.
• Counter: diccionario para llevar la cuenta de objetos hasheables

my_dict = {'key1':123,'key2':[12,23,33],'key3':['item0','item1','item2']}
my_dict['key3'][0]
Out[5]:
'item0'

my_dict['key3'][0].upper()
Out[6]:
'ITEM0'
d.keys()
d.values()

dict_items
'''

""""Pagina 50 de las diapositivas
Reimplementar las funciones que cuentan caracteres y
palabras.
 Crear una función que devuelva el diccionario inverso.
 Crear una función que gestione una agenda, permitirá agregar números de teléfono a personas.
 Crear una función que escribe una cadena en Morse.
 Crear la función inversa, de una cadena en Morse devuelve la traducción."""

#1
def cuentaGet(c):
    d = dict()
    palabras = c.split()
    for e in c:
        d[e]=d.get(e,0)+1
    print(d)

cuentaGet("holala")

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

inverso1(agenda)
inverso2(agenda)
#3
agenda = {'Luis': 689332211, 'Maria': 753951456, 'Julio': 147852654}
def añadir(agenda,n,t):
    agenda[n]=agenda.get(n, set()) | {t}

def eliminar (a,n,t):
    a[n]=a.get(n, set()) - {t}#resta de conjuntos a[n]=a.get(n, set()).remove(t)


añadir(agenda,'Raul',698352456)
eliminar(agenda,'Raul',698352456)
#4
def morse1 (cadena):
    morse = {'A': '.-', 'B': "-...", 'C': '-.-.', 'D': '-..', 'E': '.', 'F': '..-.', 'G': '--', 'H': '....', 'I': '..',
             'J': '.---', 'K': '-.-', 'L': '.-..', 'M': '--', 'N': '-.', 'Ñ': '--.--', 'O': '---', 'p': '.--.',
             'Q': '--.-',
             'R': '.-.', 'S': '...', 'T': '-', 'U': '..--', 'V': '...-', 'W': '.--', 'X': '-..-', 'Y': '-.--',
             'Z': '--..',
             '0': '-----', '1': '.----', '2': '..---', '3': ':...--', '4': '....-', '5': '.....', '6': '-....',
             '7': '--...', '8': '---..', '9': '----.', '.': '.-.-.-', ',': '-.-.--', '?': '..--..', '"': '.-..-.',
             '!': '--..--'}
    traduccido=[]
    palabras = cadena.split(" ")
    for e in palabras:
        traduccido.append(morse.get(e))
        traduccido.append(" ")
    cadena1 = ''.join(str(traduccido))
    print(traduccido)
    print(str(cadena1))
morse1("HOLA")

#5
def morse (cadena):#preguntar por que no me guarda los espacios¿
    """Funcion que recibe una frase en codigo morse y la traduce"""

    traduccido=[]
    morse = {' ':' ','.-': 'A', '-...': 'B', '-.-.': 'C', '-..': 'D', '.': 'E', '..-.': 'F', '--': 'M', '....': 'H', '..': 'I', '.---': 'J', '-.-': 'K', '.-..': 'L', '-.': 'N', '--.--': 'Ñ', '---': 'O', '.--.': 'p', '--.-': 'Q', '.-.': 'R', '...': 'S', '-': 'T', '..--': 'U', '...-': 'V', '.--': 'W', '-..-': 'X', '-.--': 'Y', '--..': 'Z', '-----': '0', '.----': '1', '..---': '2', ':...--': '3', '....-': '4', '.....': '5', '-....': '6', '--...': '7', '---..': '8', '----.': '9', '.-.-.-': '.', '-.-.--': ',', '..--..': '?', '.-..-.': '"', '--..--': '!'}
    #letras = ' '.join(cadena.split(""))
    palabras= cadena.split("/")
    print(palabras)
    for e in palabras:
        letra=e.split()
        #print(letra)
        for j in letra:
            traduccido.append(morse.get(j))
        traduccido.append("")
    cadena1= ' '.join(traduccido)
    print(traduccido)
    print(cadena1)

#morse('.... --- .-.. .-/-.-. .- .-. .-/-.-. --- .-.. .- ')

