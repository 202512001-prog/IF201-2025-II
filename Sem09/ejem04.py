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
        self.root.geometry("600x400")
        self.estudiantes = [] # arreglo de objetos
        self.estudiantes_dic = [] # arreglo de diccionarios
        self.cursos = ("TDS1", "BD1", "ADS")
        
        # --- Frame de entrada ---
        frame = tk.Frame(self.root)
        frame.pack(pady=10)
        tk.Label(frame, text="Nombre:").grid(row=0, column=0)
        tk.Label(frame, text="Edad:").grid(row=0, column=2)
        tk.Label(frame, text="Curso:").grid(row=1, column=0)
        tk.Label(frame, text="Nota:").grid(row=1, column=2)
        
        self.nombre = tk.Entry(frame)
        self.edad = tk.Entry(frame)
        self.curso = ttk.Combobox(frame, values=self.cursos) #["Matemática","Programación", "Historia"])
        self.nota = tk.Entry(frame)
        self.nombre.grid(row=0, column=1)
        self.edad.grid(row=0, column=3)
        self.curso.grid(row=1, column=1)
        self.nota.grid(row=1, column=3)
        
        tk.Button(frame, text="Agregar", command=self.agregar).grid(row=2,
        column=0, pady=5)
        tk.Button(frame, text="Eliminar",
        command=self.eliminar).grid(row=2, column=1, pady=5)
        tk.Button(frame, text="Promedio",
        command=self.promedio).grid(row=2, column=2, pady=5)
        # --- Treeview ---
        self.tree = ttk.Treeview(self.root, columns=("nombre", "edad",
        "curso", "nota"), show="headings")
        for col in self.tree["columns"]:
            self.tree.heading(col, text=col.capitalize())
            self.tree.pack(expand=True, fill="both", pady=10)
    
    def agregar(self):
        try:
            for i in range (len(self.estudiantes_dic)):
                if self.estudiantes_dic[i]["nombre"] == self.nombre.get() and self.estudiantes_dic[i]["curso"] == self.curso.get():
                    messagebox.showwarning("Alerta", "no debe ingresar valores repetidos")
                    return
            e = Estudiante(
                self.nombre.get(),
                int(self.edad.get()),
                self.curso.get(),
                float(self.nota.get())
            )
            self.estudiantes.append(e)
            self.estudiantes_dic.append({"nombre": e.nombre, "edad": e.edad, "curso": e.curso, "nota": e.nota})
            self.tree.insert("", "end", values=(e.nombre, e.edad, e.curso,
            e.nota))
        except ValueError:
            messagebox.showerror("Error", "Datos inválidos")
 
    def eliminar(self):
        selected = self.tree.selection()
        if not selected:
            messagebox.showinfo("Info", "Seleccione un registro")
            return
        for sel in selected:
            item_id = self.tree.selection()[0]
            all_items = self.tree.get_children()
            index = all_items.index(item_id)
            del self.estudiantes_dic[index]
            del self.estudiantes[index]
            self.tree.delete(sel)
    
    def promedio(self):
        if not self.estudiantes:
            messagebox.showinfo("Info", "No hay estudiantes")
            return
        notas = [e.nota for e in self.estudiantes]
        promedio = sum(notas) / len(notas)  
        messagebox.showinfo("Promedio", f"Promedio general:{promedio:.2f}\nEstudiantes: {self.estudiantes_dic}")


root = tk.Tk()
App(root)
root.mainloop()