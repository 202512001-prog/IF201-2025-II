import tkinter as tk
from tkinter import ttk, messagebox

class Archivo:
    def __init__(self, nombre):
        self.nombre_archivo = nombre
        self.arreglo = []
        
    def abrir(self):
        with open(self.nombre_archivo, 'r', encoding='UTF-8') as archivo:
            for linea in archivo:
                partes = linea.strip().split(',')      #strip: Para eliminar saltos de linea   -split: Para que identifique ','
                self.arreglo.append(partes)

    def cerrar(self):
        pass
    
    def mostrar(self):
        return self.arreglo
        
if __name__ == '__main__':
   oArch = Archivo('Producto.txt')
   oArch.abrir()
   print(oArch.mostrar())