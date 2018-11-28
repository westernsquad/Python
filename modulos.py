import statistics
import random
from datetime import datetime
import datetime
random.seed()
'''Dadas propiedades inmobiliarias con tipo y precio, calcular la
media y mediana por tipo, número de viviendas por rango de
precios y moda de todas las propiedades.'''
names ={"piso","casa","local"}
'''prop=[]
for i in range(100):
    prop.append(((random.sample(names,1)[0]),random.randint(2000,1000000)))
print (prop)
l=list()
#falta for
d=dict(zip(list(names),l))
for p in prop:
    d[p[0]].append(p[1])
for k, v in d.items():
    print (k + ": ",statistics.mean(v))
    #print (k + ": ", statistics.median(v))
    #print (k + ": ", statistics.moda(v))

#statistics.median(data)
#statistics.moda(data)'''


'''Estafa cara o cruz:
• Crear una función que simule el lanzamiento de una moneda.
• Crear una función que, mientras no se de una secuencia de cara o
cruz, siga tirando monedas.
• Modificar la función anterior para que reciba 2 secuencias de cara o
cruz, y lance monedas hasta que una de las dos se cumpla.
Cuando se cumpla devuelve la secuencia ganadora y los
lanzamientos.
• Crear una función que pida 2 secuencias y'''

def lanzar ():
    if random.randint(0,1):
        return "H"
    else:
        return "T"

def match(seq):
    s=lanzar()
    while seq not in s:
         s+=lanzar()

    return s

def match2(seq1,seq2):
    s=lanzar()
    while (seq1 and seq2) not in s:
         s+=lanzar()

    return seq1 in s

def ganadora (seq1,seq2):
    s = lanzar()
    p=0
    o=0
    while (p and o) != 100:
        if seq1 == s:
            p+=1
        elif seq2 == s:
            o+=1

        s += lanzar()


    return s

def ganadora2(seq1,seq2):
    a,b=0,0
    for i in range (100):
        if match2(seq1, seq2):
            a+=1
        else:
            b+=1

    return  a, b

s1="HHT"
s2="TTH"
a, b=ganadora2(s1,s2)
if a>b :
    print ("ha ganado:",s1,a)
else:
    print ("ha ganado: ",s2,b)
#print (match("HHT"))
#print (match2("THT","THHH"))
#print(ganadora("THT","THHH")# )


'''Crear una función que reciba una fecha (calendario gregoriano)
y devuelva el número de días desde el principio del año
(calendario juliano)'''


f = datetime.date(2018,12,31)
print(f.strftime("%j"))
