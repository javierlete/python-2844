from enum import Enum

class Estado(Enum):
    ENCENDIDO = 'on'
    APAGADO = 'off'
    INDETERMINADO = 'ox'

estado = Estado.INDETERMINADO

match estado:
    case Estado.ENCENDIDO:
        print('Hay luz')
    case Estado.APAGADO:
        print('No hay luz')
    case Estado.INDETERMINADO:
        print('Todavía no lo hemos comprobado')
