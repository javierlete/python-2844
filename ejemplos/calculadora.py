def calcular(a, op, b):
    match op:
        case '+':
            operacion = lambda x, y: x + y
        case '-':
            operacion = lambda x, y: x - y
        case _:
            raise ValueError('No se esperaba esa operacion')

    return operacion(a, b)

# Comprobación de ejecución directa desde python.exe
if __name__ == "__main__":
    import sys
    print(calcular(float(sys.argv[1]), sys.argv[2], float(sys.argv[3])))