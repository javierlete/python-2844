import sqlite3

conexion = sqlite3.connect('personas.db')
cursor = conexion.cursor()

cursor.execute("""
    CREATE TABLE IF NOT EXISTS personas (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nombre TEXT,
        apellidos TEXT
    )
""")

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
    cursor.execute("SELECT * FROM personas")

    for fila in cursor.fetchall():
        print(fila)

def buscar_por_id():
    id = int(input('Dime el id a buscar: '))

    cursor.execute(f"SELECT * FROM personas WHERE id = {id}")
    persona = cursor.fetchone()

    print(persona)

def anyadir():
    nombre = input('Nombre: ')
    apellidos = input('Apellidos: ')

    cursor.execute(f"INSERT INTO personas (nombre, apellidos) VALUES ('{nombre}', '{apellidos}')")
    conexion.commit()

    print('Persona añadida')

def modificar():
    id = int(input('Id a modificar: '))

    nombre = input('Nombre: ')
    apellidos = input('Apellidos: ')

    cursor.execute(f"UPDATE personas SET nombre = '{nombre}', apellidos = '{apellidos}' WHERE id = {id}")
    conexion.commit()

def borrar():
    id = int(input('Id a borrar: '))

    cursor.execute(f"DELETE FROM personas WHERE id = {id}")
    conexion.commit()

def salir():
    print('Gracias por usar esta aplicación')
    cursor.close()
    conexion.close()

mantenimiento()
