# CRUD: Create, Read, Update, Delete

from persona import Persona

personas = {
    1: Persona(1, 'Javier', 'Lete'),
    2: Persona(2, 'Pepe', 'Pérez')
}

print(80 * '-')

personas[2].apellidos = 'Rodríguez' # Update
personas[3] = Persona(3, 'Juan', 'González') # Create
del personas[1] # Delete

for clave in personas: # Read
    print(personas.get(clave))

print(80 * '-')

print(personas.get(3)) # Read
