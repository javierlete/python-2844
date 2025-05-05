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

import json

# Serializar a JSON (GUARDAR EN UN ARCHIVO)
with open('personas.json', 'w') as f:
    json.dump(personas, f, default=lambda p: p.__dict__, indent=4)

# Deserializar de JSON (LEER DE UN ARCHIVO)
with open('personas.json', 'r') as f:
    personas_json = json.load(f)
    
    # personas_cargadas = {
    #     int(k): Persona(**v) for k, v in personas_json.items()
    # }

    personas_cargadas = {}

    for k, v in personas_json.items():
        personas_cargadas[int(k)] = Persona(v['id'], v['nombre'], v['apellidos'])

print(80 * '-')
print('Personas cargadas')

for clave in personas_cargadas: # Read
    print(personas_cargadas.get(clave))

print(80 * '-')

import pickle

# Serializar a binario (GUARDAR EN UN ARCHIVO)
with open('personas.per', 'wb') as f:
    pickle.dump(personas, f)

# Deserializar de binario (LEER DE UN ARCHIVO)
with open('personas.per', 'rb') as f:
    personas_binario = pickle.load(f)

for clave in personas_binario: # Read
    print(personas_binario.get(clave))
