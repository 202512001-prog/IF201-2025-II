'''
Objetivo: Gestionar funciones con los datos del archivo Producto.txt
Fecha: 28-10-25
'''

import tkinter as tk 
from gestor_archivos import Archivo
from tkinter import ttk, messagebox, Menu, simpledialog

class App:
    escogidos = []
    def rango_precios(self):
        try:
            precio_minimo = simpledialog.askfloat('Dato', 'Ingrese el precio mínimo') 
            precio_maximo = simpledialog.askfloat('Dato', 'Ingrese el precio máximo')
                
        except(ValueError):
            messagebox.showerror('Error', 'Debe ingresar un valor numérico')
            return
                
        for linea in self.arreglo_datos:
            if float(linea[2]) >= precio_minimo and float(linea[2]) <= precio_maximo:
                dicc = {'Descripción': linea[2], 'precio': linea[3]}
                self.escogidos.append(dicc)
                messagebox.showinfo('Mensaje', f'Los productos cuyo precio esta entre {precio_minimo} y {precio_maximo} son:{self.escogidos} ')

    def por_descripcion(self):
        pass
    
    def precio_promedio(self):
        pass
    
    def precio_minimo_maximo(self):
        pass
    
    def descripcion_letra_inicial(self):
        pass
    
    
    def __init__(self, principal):
        self.principal = principal
        self.principal.title("Funciones con datos de productos")
        self.principal.geometry("300x200")
        self.archivo = Archivo('Producto.txt')
        self.archivo.abrir
        self.arreglo_datos = self.archivo.arreglo  # nombre correcto

        # Botones 
        self.boton_1 = tk.Button(self.principal, text='Productos entre rango de precios', command=self.rango_precios)
        self.boton_1.pack(padx=5, pady=5)
        
        self.boton_1 = tk.Button(self.principal, text='Producto por descripción', command=self.por_descripcion)
        self.boton_1.pack(padx=5, pady=5)
        
        self.boton_1 = tk.Button(self.principal, text='Precio promedio de los productos', command=self.precio_promedio)
        self.boton_1.pack(padx=5, pady=5)

        self.boton_1 = tk.Button(self.principal, text='Precio mínimo y máximo', command=self.precio_minimo_maximo)
        self.boton_1.pack(padx=5, pady=5)
        
        self.boton_1 = tk.Button(self.principal, text='Descripción que empieza con una letra', command=self.descripcion_letra_inicial)
        self.boton_1.pack(padx=5, pady=5)
        
        # Menu
        self.barra_menu = Menu(self.principal)
        self.principal.config(menu = self.barra_menu)
        
        menu_opciones = tk.Menu(self.barra_menu, tearoff=0)
        menu_opciones.add_command(label='Entre Rangos', command=self.rango_precios)
        menu_opciones.add_command(label='Por descrpción')
        menu_opciones.add_command(label='Precio promedio')
        menu_opciones.add_command(label='Precios minimos y maximos')
        menu_opciones.add_command(label='Primera letra de descripcion')

        self.barra_menu.add_cascade(label ='Opciones', menu = menu_opciones)
        
        
if __name__ == '__main__':
    root = tk.Tk()
    app = App(root)
    root.mainloop()
 