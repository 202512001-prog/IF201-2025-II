import tkinter as tk
from tkinter import ttk, messagebox
class Estudiante:
    def __init__(self, nombre, edad, curso, nota):
        self.nombre = nombre
        self.edad = edad
        self.curso = curso
        self.nota = nota
        
class App:
    def __init__(self, root):
        self.root = root
        self.root.title("Registro de Estudiantes")
        self.root.geometry("900x400")
        self.root.configure(bg = "lavender")
        self.estudiantes = [] # arreglo de objetos
        self.cursos = ('MTA','PRG','HTA')
        # --- Frame de entrada ---
        
        frame = tk.Frame(self.root, bg='lavender')
        frame.pack(pady=10)
        tk.Label(frame, text="Nombre:", bg='lavender').grid(row=0, column=0, padx=10)
        tk.Label(frame, text="Edad:", bg='lavender').grid(row=0, column=2, padx=10)
        tk.Label(frame, text="Curso:", bg='lavender').grid(row=1, column=0, padx=10)
        tk.Label(frame, text="Nota:", bg='lavender').grid(row=1, column=2, padx=10)
        
        self.nombre = tk.Entry(frame)
        self.edad = tk.Entry(frame)
        self.curso = ttk.Combobox(frame, values= self.cursos)#["Matemática", "Programación", "Historia"])
        self.nota = tk.Entry(frame)
        
        self.nombre.grid(row=0, column=1)
        self.edad.grid(row=0, column=3)
        self.curso.grid(row=1, column=1)
        self.nota.grid(row=1, column=3)
        
        frame2 = tk.Frame(self.root, bg='lavender')
        frame2.pack(pady=10)
        tk.Button(frame2, text="Agregar", command=self.agregar, bg='plum').grid(row=2, column=0, pady=5, padx=10)
        tk.Button(frame2, text="Eliminar", command=self.eliminar, bg='plum').grid(row=2, column=1, pady=5, padx=10)
        tk.Button(frame2, text="Promedio", command=self.promedio, bg='plum').grid(row=2, column=2, pady=5, padx=10)
        
        # --- Treeview ---
        self.tree = ttk.Treeview(self.root, columns=("nombre", "edad", "curso", "nota"), show="headings")
        for col in self.tree["columns"]:
            self.tree.heading(col, text=col.capitalize())
        self.tree.pack(expand=True, fill="both", pady=10)
        
    def agregar(self):
        try:
            nombre = str(self.nombre.get())
            edad = int(self.edad.get())
            curso = self.curso.get()
            nota = float(self.nota.get())

            for estudiante in self.estudiantes:
                if (estudiante.nombre == nombre and 
                    estudiante.edad == edad and
                    estudiante.curso == curso and
                    estudiante.nota == nota):
                    messagebox.showwarning("Duplicado", "Estos datos ya han sido agregados.")
                    return

            e = Estudiante(nombre, edad, curso, nota)
            self.estudiantes.append(e)
            self.tree.insert("", "end", values=(e.nombre, e.edad, e.curso, e.nota))

        except ValueError:
            messagebox.showerror("Error", "Datos inválidos")
            
    def eliminar(self):
        selected = self.tree.selection()
        if not selected:
            messagebox.showinfo("Info", "Seleccione un registro")
            return
        for sel in selected:
            self.tree.delete(sel)
            
    def promedio(self):
        if not self.estudiantes:
            messagebox.showinfo("Info", "No hay estudiantes")
            return
        
        notas = [e.nota for e in self.estudiantes]
        promedio = sum(notas) / len(notas)
        messagebox.showinfo("Promedio", f"Promedio general:{promedio:.2f}")
        

root = tk.Tk()
App(root)
root.mainloop()

# Agregar restricciones ara el nombre, las cifras de las notas, y un nuevo boton exportar