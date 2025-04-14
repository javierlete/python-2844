tablero = [
    ['t', 'c', 'a', 'k', 'q', 'a', 'c', 't'],
    ['p'] * 8,
    ['.'] * 8,
    ['.'] * 8,
    ['.'] * 8,
    ['.'] * 8,
    ['P'] * 8,
    ['T', 'C', 'A', 'K', 'Q', 'A', 'C', 'T'],
]

print(tablero)
print(tablero[0])

print(20 * '-')

print(*tablero[0])
print(*tablero[1])
print(*tablero[2])
print(*tablero[3])
print(*tablero[4])
print(*tablero[5])
print(*tablero[6])
print(*tablero[7])

print(20 * '-')

for fila in tablero:
    print(*fila)

print(20 * '-')

for fila in tablero:
    for dato in fila:
        print(dato, end=' ')
    print()

print([1, 2, 3, 4])
print(1, 2, 3 , 4)
print(*[1, 2, 3, 4])

linea = [1, 2, 3, 4, 5, 6]

for dato in linea:
    print(dato, end=';')

print()

print(*linea, sep=';')
