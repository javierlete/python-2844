from persona_avanzado import Persona

p = Persona(1, 'Javier', 'Lete')

p2 = Persona(1, 'Javier', 'Lete')

print(p)
print(p2)

print(p == p2)

p.nombre = 'Cambiado'

print(p)
print(p2)

lista = p + p2

for persona in lista:
    print(persona.nombre_completo())
