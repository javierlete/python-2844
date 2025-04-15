# Varias partidas
# Intentos
# Intentos máximos para perder

from random import randint

# Calcular un número aleatorio
numero_aleatorio = randint(1, 100)
print('Número para adivinar', numero_aleatorio)

fallado = True

while fallado:
    # Pedir un número
    texto = input('Dime un número: ')
    numero = int(texto)

    if 1 <= numero <= 100:
        # ¿Es el mismo?
        if numero == numero_aleatorio:
            print('Felicidades. Has acertado')
            fallado = False
        else:
            print('No has acertado')

            if numero_aleatorio > numero:
                print('ES MAYOR')
            else:
                print('Es menor')

    else:
        print('El número debe ser entre 1 y 100')
    # Si no volver a "pedir un número"

print('Gracias por usar este programa')
