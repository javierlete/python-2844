from persona import Persona

p1 = Persona()
print(Persona.contador)
print(p1)

p1.nombre = 'Pepe'
p1.asdf = 'Yepa'

print(p1.nombre, p1.apellidos, p1.asdf)
print(p1)

p2 = Persona(5, 'Javier', 'Lete')
print(Persona.contador)

print(p2.nombre, p2.apellidos)
print(p2)

print(p2.nombre_completo())
