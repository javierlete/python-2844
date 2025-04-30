class Botella:
    def __init__(self):
        self.abierta = False
    
    def abrir(self):
        self.abierta = True
    
    def cerrar(self):
        self.abierta = False

    def esta_abierta(self):
        return self.abierta

botella1 = Botella()
botella2 = Botella()

print(botella1.esta_abierta())
print(botella2.esta_abierta())
print(botella2.abierta)

botella1.abrir()

print(botella1.esta_abierta())
print(botella2.esta_abierta())
