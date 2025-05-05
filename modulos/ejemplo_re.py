import re

FORMATO_DNI = r'[\dXYZ]\d{7}[A-Z]'

dni_introducido = input('Dime el número de DNI: ')

if re.fullmatch(FORMATO_DNI, dni_introducido):
    print('ES UN DNI')
else:
    print('NO ES UN DNI')
