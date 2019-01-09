"""
• Dot(.): cualquier carácter excepto salto de línea (\n) . Si quiero solo un punto "\." , el \ sirve para acotar todos

• Caret(^): Inicio del string o inicio de línea. No tiene sentido con match

• Dólar($): final del string o antes de salto de línea. Asegurarme de que ya no queda nada restante.

• *: la RE previa 0 o N veces

• +: la RE previa 1 o N veces

• ?: la RE previa 0 o 1 veces. Modo no voraz.

• {m}: la RE previa exactamente m veces.

• {m, n}: la RE previa entre m y n veces.

• []: cualquiera de los caracteres en el set. Los parentesis agrupan pero ojo dentro de los corchetes
• [^]: cualquiera de los caracteres que no están en el set


• Search: busca el primer substring que cumpla el patrón.
• Findall: devuelve una lista con todos los substring.
• Sub: sustituye el substring que cumple el patrón por otro substring.
• Compile: permite preprocesar un patrón.
match para operaciones

"""
import re

# Que evalua el patron el ab* -> ab y luego muchas b
# Cadenas ab -> ab* o ab+ si no vale el vacio
# a.*c y cadena ‘abcabc’ que reconoce

def instr (str,sub):
    return str in sub

def space (str):
    new = re.sub("[][]+" , " " ,str)
    if new != str:
        return space(new)
    else:
        return new

def cuenta (str):
    return len(re.findall(r"\besta\b" , str)) #Hay que ponerlo la r delante para que no interprete las \ y mirar los \b en la documentacion (palabras)
    #\b es que el strig detecta espacios delante y detras de la palabra "esta"

def rename (list):
    '''
    renombra una lista de numeros a adenas con 0 delante
    :param list: lista de numeros
    :return: lista de cadenas
    '''
    r = []
    n=len(str((max(list))))
    for e in list:
        r.append(str(e).zfill(n+1))#rellena la cadena con 0 n+1
    return r

if __name__ == "__main__" :
    r = re.match("ab*" , "abbbbcccc")
    r2 = re.match("(ab){1,3}", "abababababab")
    print(r)
    print(r2)

    r3 = re.match("a.*c", "abcabc") #Si quiero que se pare en la primera C , con modo voraz ?
    r4 = re.match("a.*?e", "abcceabcd")#desde la a hasta la e saldran todos los caracteres que hay entre medias
    print(r4)

    # ¿Qué patrón evalúa una ‘a’ seguida de 3 o más ‘b’?

    r5 = re.match("abbb+" , "abbbaabbb") # Usar el $ para el final ò "ab{3}b*$"
    print(r5)

    # ¿Qué patrón evalúa la primera palabra de una cadena?

    r6 = re.match("[^ ]+" , "Hola que tal")
    print(r6)

    """
    – Las casillas del ajedrez están nombradas con letras(columnas) y
    números (filas). Escribe una expresión regular que evalúe si una
    cadena tiene sólo posiciones validas de ajedrez.
    """

    #Ajedrez es A a H y de 1 a 8

    r7 = re.match("([a-hA-h][1-8])+$" , "H7C3A2") #Al menos 1 vez y que $ termine, y parentesis agrupa
    print(r7)

    #Numeros en hexadecimal

    r8 = re.match("([0-9a-fA-F])+$" , "8f3") #Puede tener solo letras o solo numeros
    print(r8)

    """
    • Search: busca el primer substring que cumpla el patrón.
    • Findall: devuelve una lista con todos los substring. Cadena que no solapen, la más grande
    • Sub: sustituye el substring que cumple el patrón por otro substring. La primera aparicion la sustituye por la que le paso
    • Compile: permite preprocesar un patrón, generar el patron en una variable
    """

    #Crea una función que devuelva si una cadena es un identificador valido para una variable.

    r9 = re.match("[_]*[a-z]+[_0-9a-zA-Z]*$" , "shape") # El $ por si pones 2 palabras
    print(r9)

    #Crear una función que devuelva si una cadena es una contraseña valida con números y letras.

    r10 = re.match("[_0-9a-zA-Z]{8}[_0-9a-zA-Z]*$", "shape09898")
    print(r10)

    #– Crear una función que devuelva si una subcadena esta contenida en un string.

    r11 = re.search("[que]+" , "Holaquetal") #instr
    print(r11)

    # Crear una función que recibe una cadena y la devuelve eliminando los espacios duplicados.

    #r12 = re.sub("[][]+" , " " ,str)

    # Crear una función que devuelva cuantas veces aparece en una cadena la palabra “esta”.

    r13 = re.findall("esta" , "estasiquenoestaenestacadena esta")
    print(cuenta("esta estanteria esta estestada")) # Asi cuenta subcadenas

    #Crear una función que dada una lista de números [1, 3, 10, 23] devuelva [‘001’, ‘003’, ‘010’, ‘023’]
    list=[1,3,10,23]
    print (rename(list))

    #Crear una función que devuelva texto entrecomillado dentro de una cadena
    ree= re.findall(r'".*?"','hola "que" tal "estas".')
    re14 = re.sub(r'.*','"cadena"','hola "que" tal.')
    print (re14)
    print (ree)

    #compilado interprete mirar tipado estatico dinamico debil fuerte,
    #operadores se pueden concatenar pag 14
    #range
    #implementar pilas y colas
    #constructores de set list diccionarios
    #set tiene copy por q no tiene slide no puede recorrer
    #deccionarios si o si
    #ficheros
    #dos __ para hacer privadas las variables en una clase
    #strftime y Ttime
    #nametuple y deque
