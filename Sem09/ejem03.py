
cursos = {
 "Matemática": [("Ana", 15), ("Luis", 17), ("Marta", 14)],
 "Programación": [("Ana", 18), ("Luis", 16), ("Marta", 19)]
 }

for curso, registros in cursos.items():
    notas = [nota for _, nota in registros]
    promedio = sum(notas) / len(notas)
    print(f"Promedio en {curso}: {promedio:.2f}")    
    
# Convertir en un arreglo bidimensional
promedios = []
for curso, registros in cursos.items():
    alumno = [[curso, nota[0], nota[1]] for nota in registros]
    promedios += alumno
    print(promedios)
    