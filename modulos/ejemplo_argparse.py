import argparse

parser = argparse.ArgumentParser(
    prog='ejemplo_argparse.py',
    description='Ejemplo de uso de argparse',)

parser.add_argument('ficheros', nargs='+')
parser.add_argument('-l', '--lineas', type=int, default=10)

args = parser.parse_args()

print(args)
print(args.ficheros)
print(args.lineas)
