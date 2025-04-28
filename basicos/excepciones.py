# cuantos = int(input('¿Cuantos vienen a comer? '))
# 
# if cuantos == 0:
#     print('Entonces no hay nada que repartir')
# else:
#     print(8 / cuantos)

repetir = True

while repetir:
    try:
        cuantos = int(input('¿Cuantos vienen a comer? '))

        print(8/cuantos)
        
        repetir = False
    except ZeroDivisionError:
        print('No podemos hacer una división por cero')
    except ValueError:
        print('La próxima vez intenta un número')

print('Gracias por usar este programa')
