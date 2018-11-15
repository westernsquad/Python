def apilar(pila,elemento):
    pila.append(elemento)

def desapilar(pila):
    return pila.pop()
def cima(pila):
    return pila[-1]
def encolar(cola,elemento):
    cola.insert(0,elemento)

def desencolar (cola):
    return cola.pop
def primero(cola):
    return cola[-1]

def balanceado (cadena):
    p=[]
    for elem in cadena :
        if elem == "(":
            apilar(p,elem)
        elif elem ==")":
            desapilar(p)
    if len(p) == 0:
        return ("Es balanceado")
    else:
        return ("No esta balanceado")

string="((())"
print(balanceado(string))


def preordenIN(operator):
    if operator == '(':
        return 0
    elif operator == '+' or operator == '-':
        return 1
    elif operator == '*' or operator == '/':
        return 2
    elif operator == '^':
        return 3

def preordenOut(operator):
    if operator == '(':
        return 5
    elif operator == '+' or operator == '-':
        return 1
    elif operator == '*' or operator == '/':
        return 2
    elif operator == '^':
        return 4



def postfija (lista):
    pf=[]
    pila=[]#operadores

    for elem in lista:
        if elem.isdigit():
            pf.append(elem)
            #apilar(pf,elem)
        else:
            if len(pila)==0:
                apilar(pila,elem)
            elif elem == ")":
                while cima(pila)!="(":
                    pf.append(desapilar(pila))
                desapilar(pila)
            elif preordenIN(cima(pila)) < preordenOut(elem):
                apilar (pila,elem)
            else:
                while len(pila)!=0 and preordenIN(cima(pila)) >= preordenOut(elem):
                    pf.append(desapilar(pila))
                apilar(pila,elem)
    while len(pila)!=0 :
        pf.append(desapilar(pila))
    return pf



expresion = '4 - 5 ^ ( 5 - 2 ) + 9 * 7 - 24 / ( 7 - 2 ) '
lista = solve(expresion)
print(postfija(lista))
lista2=postfija(lista)
def calc(a,b,o):
    if o == "+":
        return str(int(a) + int(b))
    elif o == "-":
        return str(int(a) - int(b))
    elif o == "/":
        return str(int(a) // int(b))
    if o == "*":
        return str(int(a) * int(b))
    if o == "^":
        return str(int(a) ** int(b))
def resultado (lista2):
    pila = []
    po = []
    for elem in lista2:
        if elem.isdigit():
            apilar(pila,elem)
        else:
            b=desapilar(pila)
            a=desapilar(pila)
            apilar(pila,calc(a,b,elem))
        return cima(pila)
def solve(expresion):
    l=expresion.split
    print(l)
    pf= postfija(l)
    print (pf)
    return resultado(pf)
print(solve(expresion))