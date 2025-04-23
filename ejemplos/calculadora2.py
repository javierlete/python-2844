def calcular(a, op, b):
    match op:
        case '+':
            operacion = lambda x, y: x + y
        case '-':
            operacion = lambda x, y: x - y
        case _:
            raise ValueError('No se esperaba esa operacion')

    return operacion(a, b)

# a = float(input('Dime el primer operando: '))
# op = input('Dime la operación: ')
# b = float(input('Dime el segundo operando: '))

# print(calcular(a, op, b))