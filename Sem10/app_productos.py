'''
Objetivo: Gestionar los datos del archivo Producto.txt a través de una aplicación de tkinter
Fecha: 28-10-25
'''
from ejm_01 import Archivo
import tkinter as tk
from tkinter import ttk, messagebox


class Ventana:
    def __init__(self, principal):
        self.principal = principal
        self.principal.title("Gestor de archivo de productos")
        self.principal.geometry("600x400")
        self.principal.configure(bg="lavender")

        # --- Cargar datos del archivo ---
        self.archivo = Archivo('Producto.txt')
        self.archivo.abrir()
        self.arreglo_datos = self.archivo.arreglo  # nombre correcto

        # --- Variables de texto ---
        self.txtdescription = tk.StringVar()
        self.txtprecio = tk.StringVar()

        # --- Frame de entrada ---
        frame = tk.Frame(self.principal, bg='lavender')
        frame.pack(pady=10)

        tk.Label(frame, text="Código: ", bg='lavender').grid(row=0, column=0, padx=10, sticky='w')
        tk.Label(frame, text="Descripción: ", bg='lavender').grid(row=1, column=0, padx=10, sticky='w')
        tk.Label(frame, text="Precio: ", bg='lavender').grid(row=2, column=0, padx=10, sticky='w')

        self.codigo = tk.Entry(frame)
        self.lbl_description = tk.Entry(frame, textvariable=self.txtdescription)
        self.precio = tk.Entry(frame, textvariable=self.txtprecio)

        self.codigo.grid(row=0, column=1, sticky='w')
        self.lbl_description.grid(row=1, column=1, sticky='w')
        self.precio.grid(row=2, column=1, sticky='w')

        # --- Frame de botones ---
        frame2 = tk.Frame(self.principal, bg='lavender')
        frame2.pack(pady=10)

        tk.Button(frame2, text="Buscar", command=self.buscar, bg='plum').grid(row=2, column=0, pady=5, padx=10)
        tk.Button(frame2, text="Precio Menor", command=self.menor, bg='plum').grid(row=2, column=1, pady=5, padx=10)
        tk.Button(frame2, text="Sumar", command=self.sumar, bg='plum').grid(row=2, column=2, pady=5, padx=10)

        # --- Treeview ---
        self.tree = ttk.Treeview(self.principal, columns=("Código", "Descripción", "Precio"), show="headings")
        for col in self.tree["columns"]:
            self.tree.heading(col, text=col.capitalize())
        self.tree.pack(expand=True, fill="both", pady=10)

        # --- Cargar datos en Treeview ---
        self.cargar_datos()

    # --------------------------------------------------
    # FUNCIONES PRINCIPALES
    # --------------------------------------------------

    def cargar_datos(self):
        """Muestra los productos del archivo en el Treeview."""
        for fila in self.arreglo_datos:
            self.tree.insert('', tk.END, values=fila)


    def buscar(self):
        """Busca un producto por su código y muestra sus datos en los Entry y el Treeview."""
        try:
            codigo = int(self.codigo.get().strip())
        except ValueError:
            messagebox.showerror("Error", "Ingrese un código numérico válido.")
            return

        encontrado = None
        for linea in self.arreglo_datos:
            if int(linea[0]) == codigo:
                encontrado = linea
                break

        if encontrado:
            # Mostrar los datos en los Entry (usando StringVar)
            self.txtdescription.set(encontrado[1])
            self.txt.precio.set(str(encontrado[2]))

            # Mostrar solo ese producto en el Treeview
            for row in self.tree.get_children():
                self.tree.delete(row)
            self.tree.insert('', tk.END, values=encontrado)

        else:
            messagebox.showinfo("No encontrado", f"No se encontró el código {codigo}.")


    def menor(self):
        menor = 999
        for linea in self.arreglo_datos:
            if float(linea[2]) < menor:
                menor = float(linea[2])
        
        messagebox.showinfo('Mensaje', f'El precio menor en el archivo es {menor}')

    def sumar(self):
        suma = 0
        for linea in self.arreglo_datos:
            suma += float(linea[2])
            
        messagebox.showinfo('Mensaje', f'La suma de precio es {suma}')


# --- Ejecutar aplicación ---
principal = tk.Tk()
Ventana(principal)
principal.mainloop()
