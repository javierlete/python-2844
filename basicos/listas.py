nombres = ['Juan', 'Pedro', 'Pepe', 'Gonzalo']

print(nombres[0])
print(type(nombres[1]), nombres[1], nombres[3], nombres[1] + nombres[3])
print(type(nombres[1:2]), nombres[1:2], nombres[3:4], nombres[1:2] + nombres[3:4])
print(['dato'] * 5)

nombres[2] = 'Javier'

print(nombres)

pila = []

pila.append('Dato1')
pila.append('Dato3')
pila.insert(1, 'Dato2')

print(pila)

dato = pila.pop()

# append y pop crean una lista LIFO (Last In First Out) ("PILA")

print(dato)

print(pila)

cola = ['Primero', 'Colado', 'Segundo', 'Tercero']

cola.append('Cuarto')

al_cine = cola.pop(0) # Sacar elemento desde el principio

# Si usamos pop(0) funcionamos como un FIFO (First In First Out) ("COLA")

print(al_cine)

print(cola)

cola.remove('Colado')

print(cola)

del cola[1:3]

print(cola)

pila2 = pila[:]

print(pila, pila2)

del pila2[1]

print(pila, pila2)
print(id(pila), id(pila2))

lista = [1, 2, 3, 10, 7, 8, 9]

lista[3:4] = [4, 5, 6]

print(lista)