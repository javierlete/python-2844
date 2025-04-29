from persona import Persona

personas = {
    1: Persona(1, 'Javier', 'Lete'),
    2: Persona(2, 'Pepe', 'Pérez')
}

def mantenimiento():
    repetir = True

    while repetir:
        mostrar_menu()
        opcion = pedir_opcion()
        repetir = procesar_opcion(opcion)

def mostrar_menu():
    print('''
1. Listado
2. Buscar por id
3. Añadir
4. Modificar
5. Borrar

0. Salir
          ''')

def pedir_opcion():
    return int(input('Dime qué opción quieres: '))

def procesar_opcion(opcion):
    match opcion:
        case 1:
            print('LISTADO')
            listado()
        case 2:
            print('BUSCAR POR ID')
            buscar_por_id()
        case 3:
            print('AÑADIR')
            anyadir()
        case 4:
            print('MODIFICAR')
            modificar()
        case 5:
            print('BORRAR')
            borrar()
        case 0:
            print('SALIR')
            salir()
            return False
        case _:
            print('Opción incorrecta')
    
    return True

def listado():
    for persona in personas.values:
        print(persona)

def buscar_por_id():
    id = int(input('Dime el id a buscar: '))

    print(personas[id])

def anyadir():
    id = max(personas.keys()) + 1

    nombre = input('Nombre: ')
    apellidos = input('Apellidos: ')

    personas[id] = Persona(id, nombre, apellidos)

def modificar():
    id = int(input('Id a modificar: '))

    nombre = input('Nombre: ')
    apellidos = input('Apellidos: ')

    personas[id] = Persona(id, nombre, apellidos)

def borrar():
    id = int(input('Id a borrar: '))

    del personas[id]

def salir():
    print('Gracias por usar esta aplicación')

mantenimiento()
