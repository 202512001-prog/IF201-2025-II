# Aplicación principal para gestionar empleados
import tkinter as tk
from tkinter import messagebox, ttk
from gestor_archivos import Archivo
from empleado import Empleado

DEPARTAMENTOS = ('Todos', 'Sistemas', 'Recursos Humanos', 'Contabilidad', 'Marketing')

class AppEmpleados:
    def __init__(self, root):
        self.root = root
        self.root.title("Gestión de Empleados - TalentSoft")
        self.root.geometry("800x500")

        # Instancia del lector de archivos
        self.archivo = Archivo('empleados.txt')
        self.archivo.abrir()
        self.empleados = self.archivo.mostrar()

        # ComboBox para mostrar los departamentos
        tk.Label(root, text="Departamento:").grid(row=0, column=0, padx=5, pady=5)
        self.combo_departamento = ttk.Combobox(root, values=DEPARTAMENTOS)
        self.combo_departamento.grid(row=0, column=1, padx=10, pady=10)
        self.combo_departamento.current(0)

        ttk.Button(root, text="Filtrar", command=self.filtrar_por_departamento).grid(row=0, column=2, padx=5, pady=5)

        # Busqueda por nombre
        tk.Label(root, text="Buscar Nombre:").grid(row=1, column=0, padx=5, pady=5)
        self.entry_buscar = tk.Entry(root)
        self.entry_buscar.grid(row=1, column=1, padx=5, pady=5)
        ttk.Button(root, text="Buscar", command=self.buscar_por_nombre).grid(row=1, column=2, padx=5, pady=5)
    
        self.tree = ttk.Treeview(root, columns=('Código', 'Nombre', 'Iniciales', 'Departamento', 'Cargo', 'Salario'), show='headings')
        self.tree.heading('Código', text='Código', ancho='w')
        self.tree.heading('Nombre', text='Nombre', ancho='w')
        self.tree.heading('Iniciales', text='Inic.', ancho='w')
        self.tree.heading('Departamento', text='Departamento', ancho='w')
        self.tree.heading('Cargo', text='Cargo', ancho='w')
        self.tree.heading('Salario', text='Salario', ancho='w')
        # Ancho de columnas
        self.tree.column('Código', width=80, anchor='w')
        self.tree.column('Nombre', width=200, anchor='w')
        self.tree.column('Iniciales', width=80, anchor='w')
        self.tree.column('Departamento', width=150, anchor='w')
        self.tree.column('Cargo', width=150, anchor='w')
        self.tree.column('Salario', width=100, anchor='e')
        self.tree.grid(row=2, column=0, columnspan=4, padx=10, pady=10, sticky='nsew')

        self.lbl_promedio = tk.Label(root, text="Salario Promedio: $0.00", font=("Arial", 10, "bold"))
        self.lbl_promedio.grid(row=3, column=0, columnspan=4, padx=5, pady=5)

        # Botones de accion
        ttk.Button(root, text="Mostrar Promedios", command=self.mostrar_promedios).grid(row=4, column=0, padx=5, pady=5, sticky='e')
        ttk.Button(root, text="Aumentar Salario (10%)", command=self.aumentar_salario).grid(row=4, column=1, padx=5, pady=5, sticky='e')      
        ttk.Button(root, text="Cargar Archivo", command=self.cargar_archivo).grid(row=4, column=3, padx=5, pady=5, sticky='e')  
        #self.cargar_empleados()
        
    def cargar_empleados(self):
        for emp in self.empleados:
            if emp.salario == self.salario_maximo():
                emp.nombre = emp.nombre.upper()
                self.tree.insert('', tk.END, values=(emp.codigo, emp.nombre, self.iniciales(emp.nombre), emp.departamento, emp.cargo, f"${emp.salario:.2f}"))
    
    def iniciales(self, nombre):
        partes = nombre.split()
        iniciales = ''.join([p[0].upper() for p in partes])
        return iniciales
    
    def salario_maximo(self):
        if not self.empleados:
            return 0
        return max(emp.salario for emp in self.empleados)
    
    def cerrar(self):
        self.archivo.cerrar()

    def cargar_archivo(self):
        self.cargar_empleados()
        self.filtrar_por_departamento()
        messagebox.showinfo("Carga de Archivo", "Archivo de empleados cargado correctamente.")


    def aumentar_salario(self):
        for emp in self.empleados:
            emp.aumentar_salario(10)
        
        # Actualizar la vista
        self.filtrar_por_departamento()
        messagebox.showinfo("Aumento de Salario", "Se ha aumentado el salario de todos los empleados en un 10%.")
        self.mostrar_promedios()

    def mostrar_promedios(self):
        total_salario = sum(emp.salario for emp in self.empleados)
        promedio = total_salario / len(self.empleados) if self.empleados else 0
        self.lbl_promedio.config(text=f"Salario Promedio: ${promedio:.2f}")

        deptos = {}
        for emp in self.empleados:
            deptos.setdefault(emp.departamento, []).append(emp.salario)

        texto = "\n".join([f"{d}: S/. {sum(v)/len(v):.2f}" for d, v in deptos.items()])
        messagebox.showinfo("Promedio de salarios por departamento", texto)
        
        self.promedio_departamento ={d: sum(v)/len(v) for d, v in deptos.items()}
        if self.promedio_departamento:
            depto_menor_promedio = min(self.promedio_departamento, key=self.promedio_departamento.get)
            messagebox.showinfo('Departamento de menor promedio', f'El departamento con menor promedio es {depto_menor_promedio.lower()} con ${self.promedio_departamento[depto_menor_promedio]}')
        

    def buscar_por_nombre(self):
        texto_buscar = self.entry_buscar.get().strip().lower()
        self.tree.delete(*self.tree.get_children())
        for emp in self.empleados:
            if emp.salario == self.salario_maximo():
               emp.nombre = emp.nombre.upper()
            if texto_buscar in emp.nombre.lower():
                self.tree.insert('', tk.END, values=(emp.codigo, emp.nombre, self.iniciales(emp.nombre), emp.departamento, emp.cargo, f"${emp.salario:.2f}"))

    def filtrar_por_departamento(self):
        departamento_seleccionado = self.combo_departamento.get()
        # Limpiar el Treeview
        for item in self.tree.get_children():
            self.tree.delete(item)
        
        for emp in self.empleados:
            if emp.salario == self.salario_maximo():
               emp.nombre = emp.nombre.upper()
            if departamento_seleccionado == 'Todos' or emp.departamento == departamento_seleccionado:
                self.tree.insert('', tk.END, values=(emp.codigo, emp.nombre, self.iniciales(emp.nombre), emp.departamento, emp.cargo, f"${emp.salario:.2f}"))

if __name__ == '__main__':
    root = tk.Tk()
    app = AppEmpleados(root)
    root.mainloop()
   
   