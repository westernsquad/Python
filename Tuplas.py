'''• Set:
– Colección desordenada y mutable de objetos hasheables.
– Para crear un set, elementos entre llaves ({}).
s = {“A”, “B”, 3}
– También existe el constructor set().
s1 = set() # set vacio
s2 = set(“A”, “B”, 3)
– Como el resto de colecciones, soporta:
len(s1) # longitud
x in s2 # consulta
 for e in s: # iterar
– Para modificar el conjunto:
s.add(“C”) # añade “C” al conjunto
s.pop() # devuelve uno de sus elementos y lo elmina
s.remove(“B”) # elimina el elemento “B”
****************************************************************************************************
• Set 2:
– Los set, al ser mutables, no son hasheables.
– Los frozenset son set inmutables.
s = frozenset(1, 2, 4)
– Operadores de comparación en set, isdisjoint(), <, >.
s1.issubset(s2) # s1 <= s2
s2.issuperset(s1) # s2 >= s1
– Constructoras no generadoras:
s3 = s1.union(s2) # s3 = s1 | s2
s3 = s1.intersection(s2) # s3 = s1 & s2
s3 = s1.difference(s2) # s3 = s1 - s2
– Copiar un conjunto:
s2 = s1.copy()
*****************************************************************************************************
Tuplas:
– Son colecciones heterogéneas, ordenadas e inmutables, una
agrupación de elementos.
t = (‘Hola’, 4)
print(t)
– Se puede acceder a sus elementos.
print(t[0])
– Se pueden desempaquetar.
text, number = t
print(number)
– Para saber el número de elementos len().
– Como toda colección, se puede iterar en un bucle for.
for e in t:
print(e)'''
''' 
**********************************************************
• Slice:
– Se puede acceder a un elemento de un contenedor:
a = (1, ‘Hola’, 3.5) # a[1] = ‘Hola’
– Si se intenta acceder fuera de rango Python fallará.
– Si se usa un indice negativo, se accede por el final:
a[-1] # 3.5
– Utilizando el operador “:” se puede acceder a rangos de valores:
“Hola”[0:2] # ‘Ho’
“Hola”[1:3] # ‘ol’
“Hola”[1:] # ‘ola’
“Hola”[:] # ‘Hola’
“Hola”[::2] # ‘Hl’
– Si el contenedor es mutable, se puede reescribir el subrango:
[0, 1, 2, 3][::2] = [4, 6] # [4, 1, 6, 3]
'''