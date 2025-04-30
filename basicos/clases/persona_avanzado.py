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
    
    @property
    def id(self):
        return self.__id
    
    @id.setter
    def id(self, nuevo_id):
        self.__id = nuevo_id

    @property
    def nombre(self):
        return self.__nombre  # Getter

    @nombre.setter
    def nombre(self, nuevo_nombre):
        if nuevo_nombre.strip():  # Validación
            self.__nombre = nuevo_nombre
        else:
            raise ValueError("El nombre no puede estar vacío")

    @property
    def apellidos(self):
        return self.__apellidos  # Getter

    @apellidos.setter
    def apellidos(self, nuevos_apellidos):
        self.__apellidos = nuevos_apellidos

    def nombre_completo(self):
        return f'{self.nombre} {self.apellidos}'

    def __add__(self, other):
        return [self, other]

    def __eq__(self, value):
        if self.id != value.id:
            return False
        
        if self.nombre != value.nombre:
            return False
        
        if self.apellidos != value.apellidos:
            return False
                
        return True
    
        # return self.id == value.id and self.nombre == value.nombre and self.apellidos == value.apellidos

    # Conversión a texto del objeto
    def __str__(self):
        '''Conversión a texto del objeto'''
        return f'{self.id=}, {self.nombre=}, {self.apellidos=}'
