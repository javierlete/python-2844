from persona_avanzado import Persona

class Empleado(Persona):
    '''Clase que representa un empleado que tiene nombre, apellidos y salario'''

    # Variables de clase (compartidas)
    SALARIO_POR_DEFECTO = 1000.0

    def __init__(self, id=None, nombre=Persona.NOMBRE_POR_DEFECTO, apellidos=Persona.APELLIDOS_POR_DEFECTO, salario=SALARIO_POR_DEFECTO):
        '''Constructor'''
        super().__init__(id, nombre, apellidos)  # Llamada al constructor de la clase padre
        self.salario = salario  # Variable de instancia

    @property
    def salario(self):
        return self.__salario  # Getter

    @salario.setter
    def salario(self, nuevo_salario):
        if isinstance(nuevo_salario, (int, float)) and nuevo_salario >= 0:
            self.__salario = nuevo_salario
        else:
            raise ValueError("El salario no puede ser negativo y debe ser un número")