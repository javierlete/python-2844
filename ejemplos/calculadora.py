a = float(input('Dime el primer operando: '))
op = input('Dime la operación: ')

match op:
    case '+':
        operacion = lambda x, y: x + y
    case '-':
        operacion = lambda x, y: x - y
    case _:
        raise ValueError('No se esperaba esa operacion')

b = float(input('Dime el segundo operando: '))

print(operacion(a, b))