from persona import Persona

personas = {}

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
6. Cargar
7. Guardar
8. Importar JSON
9. Exportar JSON

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
        case 6:
            print('CARGAR')
            cargar()
        case 7:
            print('GUARDAR')
            guardar()
        case 8:
            print('IMPORTAR JSON')
            importar_json()
        case 9:
            print('EXPORTAR JSON')
            exportar_json()
        case 0:
            print('SALIR')
            salir()
            return False
        case _:
            print('Opción incorrecta')
    
    return True

def listado():
    if not personas:
        print('No hay personas')
        return
    
    for persona in personas.values():
        print(persona)

def buscar_por_id():
    id = int(input('Dime el id a buscar: '))

    print(personas[id])

def anyadir():
    # id = max(personas.keys()) + 1 if personas else 1
    
    id = 1

    if personas:
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

def cargar():
    global personas
    
    import pickle
    with open('personas.per', 'rb') as f:
        personas = pickle.load(f)

def guardar():
    import pickle
    with open('personas.per', 'wb') as f:
        pickle.dump(personas, f)

def importar_json():
    global personas

    personas = {}

    import json
    with open('personas.json', 'r') as f:
        personas_json = json.load(f)
        for id, persona in personas_json.items():
            personas[int(id)] = Persona(int(id), persona['nombre'], persona['apellidos'])

def exportar_json():
    import json
    with open('personas.json', 'w') as f:
        personas_json = {id: {'nombre': persona.nombre, 'apellidos': persona.apellidos} for id, persona in personas.items()}
        json.dump(personas_json, f)

def salir():
    print('Gracias por usar esta aplicación')

mantenimiento()
