var = 5

print(f'La var vale {var}')
print(f'{var}')
print(f'{var=}')

x = 10
y = 20

print(f'{x=}, {y=}, {x*y=}')

lista = [ 1, -56, 1_234, -23, 21_346, 234 ]

print('  Valores')

for dato in lista:
    print('{:9}'.format(dato))

lista = [ .05_2, -.78_3, .34_6, .68_2 ]

for dato in lista:
    print(f'{dato:9.2%}')

print('{1:5}, {0:5}'.format(10, 11))

print('5')
print(str(5))
print(repr('5'))

import math

print(f'{math.pi:.2f}')

