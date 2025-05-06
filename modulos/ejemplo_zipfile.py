from zipfile import ZipFile
from glob import glob

with ZipFile('modulos/ejemplo.zip', 'w') as archivo_zip:
    for fichero in glob('modulos/ejemplo_*'):
        archivo_zip.write(fichero)

with ZipFile('modulos/ejemplo.zip', 'r') as archivo_zip:
    # Extraer todos los ficheros en la carpeta actual
    # archivo_zip.extractall()
    # Extraer un fichero específico
    # archivo_zip.extract('modulos/ejemplo_urllib.py')
    # Listar el contenido del zip
    print(archivo_zip.namelist())
