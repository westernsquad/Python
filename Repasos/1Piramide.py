'''Dada una altura, pintar una pirámide como la siguiente:
  *
 ***
*****'''

n=3
for i in range(n):
    print(' '*(n-i) + '*'*(2*i+1))


print('********************************************')
''' ¿Cómo pintarías una pirámide invertida?'''
n=3
for i in range (n):
    print(' '*(i+1-1)+ '*'*((n-i)*2-1))

n=3
for i in range (n-1,-1,-1):
    print(' '*(n-i) + '*'*(2*i+1))


#Pinta un rombo.
print('Rombo')

a=3
for i in range (a):
    print(' ' * (a - i) + '*' * (2 * i + 1))

for i in range(a - 2, -1, -1):
    print(' ' * (a - i) + '*' * (2 * i + 1))
