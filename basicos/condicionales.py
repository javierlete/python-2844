nombre = input('Dime tu nombre: ')

print(nombre == 'Javier')

if nombre == 'Javier':
    print('Hombre, el profe')
elif nombre == 'Pepe':
    print('Hombre... un ejemplo con patas')
else:
    print('Pues debes ser otra persona')

print('Hola ' + nombre)

match nombre:
    case 'Javier':
        print('Hombre, el profe')
    case 'Pepe':
        print('El ejemplo con patas')
    case _:
        print('No te conozco')

punto = (5, 9)

match punto:
    case (0, 0):
        print('Origen de coordenadas')
    case (x, 0):
        print(f'La x vale {x}')
    case (0, y):
        print(f'La y vale {y}')
    case (x, y):
        print(f'P({x}, {y})')
    case _:
        raise ValueError('No es un punto')