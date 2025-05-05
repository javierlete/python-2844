import sys

print(sys.argv)

if len(sys.argv) != 3:
    sys.stderr.write("Uso: python ejemplo_sys.py <num1> <num2>")
    sys.exit(1)

a = int(sys.argv[1])
b = int(sys.argv[2])

c = a + b

print(f"La suma de {a} + {b} es {c}")

