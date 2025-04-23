def formato_punto(punto: tuple = (0,0)) -> str:
    '''Esta función devuelve un texto con formato basado en el punto recibido'''
    (x, y) = punto

    return f'Punto[{x}, {y}]'

def mostrar_punto(punto: tuple = (0,0)) -> None:
    '''Muestra por consola el punto con el formato de formato_punto'''
    print(formato_punto(punto))

punto1 = (5, 6)
punto2 = (1, 2)

mostrar_punto(punto1)
mostrar_punto(punto2)

print(formato_punto(punto1))
print(formato_punto(punto2))

mostrar_punto()

def intercambia(x, y):
    return y, x

a, b = 1, 2

print('a, b', a, b)

c, d = intercambia(a, b)

print('c, d', c, d)

def ask_ok(prompt, retries=4, reminder='Please try again!'):
    while True:
        reply = input(prompt)
        if reply in {'y', 'ye', 'yes'}:
            return True
        if reply in {'n', 'no', 'nop', 'nope'}:
            return False
        retries = retries - 1
        if retries < 0:
            raise ValueError('invalid user response')
        print(reminder)

# ask_ok('¿Estás seguro?')
# ask_ok('¿Estás seguro?', 2)
# ask_ok('¿Estás seguro?', 2, 'Inténtalo de nuevo')

# ask_ok(reminder='Ten cuidado', prompt='¿Estás seguro?', retries = 2)

def carrito(articulo, articulos=[]):
    articulos.append(articulo)
    return articulos

carrito('Pan')
carrito('Pescado')
print(carrito('Ensalada'))

def lista_argumentos_variable(*argumentos):
    print('LISTA')
    for arg in argumentos:
        print(arg, end=',')

lista_argumentos_variable()
lista_argumentos_variable(1, 2, 3)
lista_argumentos_variable('Hola', 'Que', 'Tal', 'Vosotros')

def sumatorio(*numeros):
    total = 0
    for numero in numeros:
        total += numero
    
    return total

print(sumatorio(1, 2, 3, 4))
print(sumatorio(5, 6))

diccionario = { 'clave': 'valor', 'casa': 'home', 'perro': 'dog' }

print(diccionario['perro'])

def crea_diccionario(**pares):
    resultado = {}

    for clave in pares:
        resultado[clave] = pares[clave]
    
    return resultado

res = crea_diccionario(telefono = 'phone', teclado = 'keyboard')

print(res['teclado'])

def cheeseshop(kind, *arguments, **keywords):
    print("-- Do you have any", kind, "?")
    print("-- I'm sorry, we're all out of", kind)
    for arg in arguments:
        print(arg)
    print("-" * 40)
    for kw in keywords:
        print(kw, ":", keywords[kw])

cheeseshop('sausage', 'Pues vaya', 'Ya te vale', 'Ya podrías tener', cliente='Javier', vendedor='Python')

def combined_example(pos_only, /, standard1, standard2, *, kwd_only):
    print(pos_only, standard1, standard2, kwd_only)

combined_example(5, 6, 7, kwd_only = 8)
combined_example(5, 6, standard2 = 7, kwd_only = 8)
combined_example(5, standard1 = 6, standard2 = 7, kwd_only = 8)

def funcion(a, b, c):
    print(a, b, c)

funcion(1, 2, 3)

lista = [4, 5, 6]
funcion(*lista) # funcion(4, 5, 6)

diccionario = { 'a': 7, 'b': 8, 'c': 9 }
funcion(**diccionario) # funcion(a = 7, b = 8, c = 9)

operacion = lambda a, b: a + b # def operacion(a, b): return a + b

print(operacion(2, 3))

operacion = lambda a, b: a - b

print(operacion(2, 3))
