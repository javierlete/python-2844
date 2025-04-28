with open('fichero.txt', 'w', encoding="utf-8") as f:
    f.write('Hola a todos\n')
    f.write('Este es mi primer fichero escrito desde Python\n')

with open('fichero.txt', 'r', encoding="utf-8") as f:
    contenido_completo = f.read()
    
    print(contenido_completo)

with open('fichero.txt', 'r', encoding="utf-8") as f:
    numero = 1
    
    for linea in f:
        print(numero, end=':')
        
        for caracter in linea:
            if caracter == '\n':
                print(caracter, end='')
            else:
                print(caracter, end='.')
        
        numero += 1
