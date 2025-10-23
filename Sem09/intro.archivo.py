"""
Objetivo: Introducción en la gestión de archivos de texto
Fecha: 23-10-2025
"""

# Operación de lectura
with open('datos.txt', 'r', encoding = 'UTF-8') as archivo:
    contenido = archivo.read()
    print(contenido)

    archivo.close()

# Lectura línea por línea     
with open('datos.txt', encoding='UTF-8') as archivo:
    for linea in archivo:
        print(linea.strip())
        
    archivo.close()

# Creaccion de un diccionario a partir de la lectura de datos  
with open('datos.txt', encoding='UTF-8') as archivo:
    distritos = []
    for linea in archivo:
        print(f'Contenido de la línea: {linea.strip()} ')
        partes = linea.strip().split(',') # partes[0] = 1  partes[1] = 'Lima'
        print('{' + f'Código: {partes[0]}, Nombre:{partes[1]}' + '}')
        distritos.append({'Código': int(partes[0]), 'Nombre':partes[1]})
        
    archivo.close()
    print(distritos)
        
# Ingrese un numero entre 1 y 2 usando el arreglo distritos busque el elemento cuyo codigo sea igual al
# numero    
    
    numero = int(input(('Ingrese un número: ')))
    for i in range(len(distritos)):
        if numero == distritos[i]['Código']:
            print(f'Corresponde al distrito: {distritos[i]['Nombre']}')
