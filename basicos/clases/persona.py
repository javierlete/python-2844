class Persona:
    '''Clase que representa una persona que tiene nombre y apellidos'''

    # Variables de clase (compartidas)
    NOMBRE_POR_DEFECTO = 'Juan'
    APELLIDOS_POR_DEFECTO = 'Nadie'

    contador = 0

    def __init__(self, id = None, nombre = NOMBRE_POR_DEFECTO, apellidos = APELLIDOS_POR_DEFECTO):
        '''Constructor'''
        # Variables de instancia
        self.id = id
        self.nombre = nombre
        self.apellidos = apellidos

        Persona.contador += 1
    
    def nombre_completo(self):
        return f'{self.nombre} {self.apellidos}'

    # Conversión a texto del objeto
    def __str__(self):
        '''Conversión a texto del objeto'''
        return f'{self.id=}, {self.nombre=}, {self.apellidos=}'
