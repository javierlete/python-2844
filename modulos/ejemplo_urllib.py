import re
from urllib.request import urlopen

resultados = []

partido = {}

with urlopen('https://www.resultados-futbol.com/') as respuesta:
    for linea in respuesta:
        linea = linea.decode()
        if 'dlc' in linea:
            datos = re.findall(r'>(.*?)<', linea)
            for dato in datos:
                if dato.strip():  # Ignorar datos vacíos
                    # print('dlc', dato)
                    partido['invitado'] = dato.strip()
        if 'hlc' in linea:
            datos = re.findall(r'>(.*?)<', linea)
            for dato in datos:
                if dato.strip():
                    # print('hlc', dato)
                    partido['local'] = dato.strip()
        if 'marker_box' in linea:
            datos = re.findall(r'<div.*>(.*?)</div>', linea)
            for dato in datos:
                if dato.strip():
                    # print('marker_box', dato)
                    partido['resultado'] = dato.strip()

        if all(key in partido for key in ['local', 'invitado', 'resultado']):
            resultados.append(partido.copy())
            partido.clear()

print(resultados)

for partido in resultados:
    resultado_local = partido['resultado'].split('-')[0]
    resultado_invitado = partido['resultado'].split('-')[1]
    
    if int(resultado_local) >= 3 or int(resultado_invitado) >= 3:
        print(f"{partido['local']:30} |{partido['resultado']}| {partido['invitado']:30}")