alumnos = ['Ana','Luis','Marta']
notas = [
    [15, 17, 14, 13], # Notas de Ana
    [13, 16, 18, 13, 14], # Notas de Luis
    [20, 19, 18] # Notas de Marta  
]

for i in range(len(alumnos)):
 promedio = sum(notas[i]) / len(notas[i])
 print(f"{alumnos[i]} tiene un promedio de {promedio:.2f}")

# Diccionario 
resultados = {alumnos[i]: sum(notas[i]) / len(notas[i]) for i in range(len(alumnos))}
print(resultados)

# Tupla

# Arreglo
promedio = [(alumnos[i], sum(notas[i]) / len(notas[i])) for i in range(len(alumnos))]
print(promedio)
 