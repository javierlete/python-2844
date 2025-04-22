contador = 1

while contador <= 10:
    print(contador, end=' ')
    contador = contador + 1

print()

for dato in range(1, 11):
    print(dato, end=' ')

print()

for dato in range(10, 0, -1):
    print(dato, end=' ')

lista = [1, 5, 78, 3, 5]

print()

for dato in lista:
    match dato:
        case 4:
            print('Encontrado 4')
            break
        case 6:
            print('Encontrado 6')
            break
else:
    print('NO encontrado')

