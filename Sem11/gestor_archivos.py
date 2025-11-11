'''
    Objetivo: Gestionar archivos, solo para lectura del contenido
    Fecha: 28-10-2025
'''
from empleado import Empleado

class Archivo:
    def __init__(self, nombre):
        self.nombre_archivo = nombre
        self.arreglo = []
        
    def abrir(self):
        with open(self.nombre_archivo, 'r', encoding='UTF-8') as archivo:
            for linea in archivo:
                partes = linea.strip().split(';')
                empleado = Empleado(partes[0], partes[1], partes[2], partes[3], partes[4])
                self.arreglo.append(empleado)

    def __str__(self):
        salida = ""
        for emp in self.arreglo:
            salida += str(emp) + "\n"
        return salida
    
    def cerrar(self):
        pass
    
    def mostrar(self):
        return self.arreglo
    
if __name__ == '__main__':
    oArch = Archivo('empleados.txt') 
    
    oArch.abrir()
    print(oArch)