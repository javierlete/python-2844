import os

# Obtener el nombre del sistema operativo
print(os.name)

# Obtener el directorio de trabajo actual
print(os.getcwd())

# Cambiar el directorio de trabajo
os.chdir('../Documents')
print(os.getcwd())

os.system('ECHO Hola Mundo')
os.system('DIR')
