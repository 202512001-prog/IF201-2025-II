class Paciente:
    def __init__(self, id, nombre, edad, diagnostico, especialidad, costo):
        self.id = id
        self.nombre = nombre
        self.edad = int(edad)
        self.diagnostico = diagnostico
        self.especialidad = especialidad
        self.costo = float(costo)

    def __str__ (self):
        return f'{self.id} - {self.nombre} | {self.edad} años | {self.diagnostico} | {self.especialidad} | S/ {self.costo:.2f}'
     
    def iniciales(self):
        return ''.join([parte[0].upper() for parte in self.nombre.split()])