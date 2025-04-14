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