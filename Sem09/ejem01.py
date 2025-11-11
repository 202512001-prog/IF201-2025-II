alumnos = ['Jhassmin', 'Andre', 'Jungwon']
notas = [
    [15, 17, 20, 16], # Notas de Jhassmin
    [14, 18, 20, 18, 15], # Notas de Andre
    [14, 15, 18]  # Notas de Jungwon
]

for i in range (len(alumnos)):
    promedio = sum(notas[i])/len(notas[i])
    print(f'{alumnos[i]} tiene un promedio de {promedio:.2f}')

# Como diccionario
prom_alumnos = {alumnos[i]: round(sum(notas[i]) / len(notas[i]), 2) for i in range (len(alumnos))}
print(prom_alumnos)

# Tupla
tupla_prom = tuple((alumnos[i], round(sum(notas[i]) / len(notas[i]), 2)) for i in range (len(alumnos)))
print(tupla_prom)



print('# ----------------------------------------------------- #')



cursos = {
    'Matemática': [('Ana', 15), ('Luis', 17), ('Marta', 14)],
    'Programación': [('Ana', 18), ('Luis', 16), ('Marta', 19)],
    'Física': [('Ana', 16), ('Luis', 18), ('Marta', 12)]
}

for curso, registros in cursos.items():
    notas = [nota for _, nota in registros]
    promedio = sum(notas) / len (notas)
    print(f'Promedio en {curso}: {promedio:.2f}')

# Convertir a un arreglo bidimensional
arre_bidimen = []
for curso, registros in cursos.items():
    datos_alumno = [[curso, dato[0], dato[1]] for dato in registros]
    arre_bidimen += datos_alumno
print(arre_bidimen)


print('# ----------------------------------------------------- #')

# Para mostrar tal arreglo en formato tabla
for fila in arre_bidimen:
    print(fila)


print('# ----------------------------------------------------- #')

# Para hacerlo mas visual
print('Curso          Alumno          Nota')
print('-----------------------------------')
for curso, alunmo, dato in arre_bidimen:
    print(f'{curso:<15}{alunmo:<17}{dato}')

 