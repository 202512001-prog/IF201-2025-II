# empleado.py
class Empleado:
    def __init__(self, codigo, nombre, departamento, cargo, salario):
        self.codigo = codigo
        self.nombre = nombre
        self.departamento = departamento
        self.cargo = cargo
        self.salario = float(salario)

    def __str__(self):
        return f"{self.codigo} - {self.nombre} - {self.departamento} - {self.cargo} - ${self.salario:.2f}"
    
    def iniciales(self):
        nombres = self.nombre.split()
        iniciales = ''.join([n[0].upper() + '.' for n in nombres])
        return iniciales

    def aumentar_salario(self, porcentaje):
        self.salario += self.salario * (porcentaje / 100)   
    
if __name__ == '__main__':
    emp = Empleado("COD001", "Ana Torres", "Sistemas", "Analista", 4800.50)
    print(emp)
    print("Iniciales:", emp.iniciales())
    emp.aumentar_salario(10)
    print("Salario después del aumento:", emp.salario)