# import calculadora
# import calculadora as c
# from calculadora import calcular
# from calculadora import *
from calculadora import calcular as calc

a = float(input('Dime el primer operando: '))
op = input('Dime la operación: ')
b = float(input('Dime el segundo operando: '))

# print(calculadora.calcular(a, op, b))
# print(c.calcular(a, op, b))
# print(calcular(a, op, b))
print(calc(a, op, b))
