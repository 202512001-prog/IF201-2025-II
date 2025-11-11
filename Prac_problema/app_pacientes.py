import tkinter as tk
from tkinter import ttk, messagebox
from archivo_pacientes import Archivo  # clase que maneja lectura de pacientes desde archivo


class AppPacientes:
    def __init__(self, root):
        self.root = root
        self.root.title("Gestión de Pacientes")
        self.root.geometry("862x576")
        self.root.configure(bg="#ffe6f2")  # Fondo rosado claro y elegante

        # --- Leer datos del archivo ---
        self.archivo = Archivo('pacientes.txt')
        self.archivo.abrir()
        self.pacientes = self.archivo.mostrar()

        # --- Filtros por especialidad ---
        tk.Label(root, text="Especialidad:", bg="#ffe6f2", fg="#8b0066", font=("Arial", 10, "bold")).grid(row=0, column=0, padx=10, pady=10, sticky="w")

        especialidades = sorted(list({p.especialidad for p in self.pacientes}))
        especialidades.insert(0, "Todos")  # opción para ver todos los pacientes
        self.combo_especialidad = ttk.Combobox(root, values=especialidades, state="readonly", width=25)
        self.combo_especialidad.grid(row=0, column=1, padx=5, pady=10)
        self.combo_especialidad.current(0)
        self.combo_especialidad.bind("<<ComboboxSelected>>", self.filtrar)

        # --- Botón para mostrar promedios ---
        tk.Button(root, text="Mostrar Promedios", bg="#ff99cc", command=self.mostrar_promedios).grid(row=0, column=2, padx=10, pady=10)

        # --- Crear tabla Treeview ---
        columnas = ("ID", "Nombre", "Edad", "Diagnóstico", "Especialidad", "Costo", "Iniciales")
        self.tree = ttk.Treeview(root, columns=columnas, show="headings", height=15)
        self.tree.grid(row=1, column=0, columnspan=4, padx=10, pady=10)

        # --- Encabezados de la tabla ---
        for col in columnas:
            self.tree.heading(col, text=col)
            self.tree.column(col, width=120, anchor="center")

        # --- Estilo para Treeview ---
        estilo = ttk.Style()
        estilo.configure("Treeview",
                         background="#fff0f5",  # rosa pálido
                         foreground="black",
                         rowheight=25,
                         fieldbackground="#fff0f5")
        estilo.map("Treeview", background=[("selected", "#ffb6c1")])  # rosa más fuerte al seleccionar

        # --- Cargar datos en tabla ---
        self.cargar_datos(self.pacientes)

        # --- Etiquetas de resultados ---
        self.lbl_mayor = tk.Label(root, text="", bg="#ffe6f2", fg="#cc0066", font=("Arial", 10, "bold"))
        self.lbl_mayor.grid(row=2, column=0, columnspan=2, sticky="w", padx=10, pady=5)

        self.lbl_menor = tk.Label(root, text="", bg="#ffe6f2", fg="#cc0066", font=("Arial", 10, "bold"))
        self.lbl_menor.grid(row=3, column=0, columnspan=2, sticky="w", padx=10, pady=5)

        self.lbl_menor_esp = tk.Label(root, text="", bg="#ffe6f2", fg="#cc0066", font=("Arial", 10, "bold"))
        self.lbl_menor_esp.grid(row=4, column=0, columnspan=3, sticky="w", padx=10, pady=5)

        # --- Mostrar resultados iniciales ---
        self.actualizar_etiquetas()

    # ======================================================
    # MÉTODOS DE PROCESAMIENTO DE DATOS
    # ======================================================

    def cargar_datos(self, lista):
        """Carga los datos de pacientes al TreeView."""
        self.tree.delete(*self.tree.get_children())  # limpia la tabla antes de cargar

        paciente_max = self.paciente_mayor_costo()  # para resaltar fila

        for p in lista:
            costo = float(p.costo)
            tag = "normal"
            if p == paciente_max:
                tag = "mayor"  # etiqueta especial para color

            # insertar paciente en la tabla
            self.tree.insert("", tk.END, values=(p.id, p.nombre, p.edad, p.diagnostico, p.especialidad, f"S/ {costo:.2f}", p.iniciales()), tags=(tag,))

        # Color especial para el paciente con mayor costo
        self.tree.tag_configure("mayor", background="#ffd6e7", foreground="black")

    def filtrar(self, event):
        """Filtra pacientes por especialidad seleccionada."""
        esp = self.combo_especialidad.get()
        if esp == "Todos":
            lista = self.pacientes
        else:
            lista = [p for p in self.pacientes if p.especialidad == esp]
        self.cargar_datos(lista)

    def paciente_mayor_costo(self):
        """Devuelve el paciente con mayor costo."""
        return max(self.pacientes, key=lambda p: float(p.costo))

    def paciente_menor_costo(self):
        """Devuelve el paciente con menor costo."""
        return min(self.pacientes, key=lambda p: float(p.costo))

    def promedio_por_especialidad(self):
        """Calcula el promedio de costo por especialidad."""
        promedios = {}
        for p in self.pacientes:
            esp = p.especialidad
            promedios.setdefault(esp, []).append(float(p.costo))
        for esp in promedios:
            promedios[esp] = sum(promedios[esp]) / len(promedios[esp])
        return promedios

    def especialidad_promedio_mas_bajo(self):
        """Devuelve la especialidad con menor promedio."""
        promedios = self.promedio_por_especialidad()
        return min(promedios, key=promedios.get)

    def actualizar_etiquetas(self):
        """Actualiza las etiquetas de los resultados principales."""
        p_mayor = self.paciente_mayor_costo()
        p_menor = self.paciente_menor_costo()
        esp_menor = self.especialidad_promedio_mas_bajo()

        # Mostrar los resultados pedidos (a–f)
        self.lbl_mayor.config(text=f"Paciente mayor costo: {p_mayor.nombre.upper()} | Diagnóstico: {p_mayor.diagnostico.upper()}")
        self.lbl_menor.config(text=f"Paciente menor costo: {p_menor.nombre} | Costo: S/ {float(p_menor.costo):.2f}")
        self.lbl_menor_esp.config(text=f"Especialidad con menor promedio: {esp_menor.lower()}")

    def mostrar_promedios(self):
        """Muestra los promedios de costo por especialidad en una ventana emergente."""
        promedios = self.promedio_por_especialidad()
        texto = "PROMEDIOS POR ESPECIALIDAD:\n\n"
        for esp, prom in promedios.items():
            texto += f"{esp}: S/ {prom:.2f}\n"
        messagebox.showinfo("Promedios", texto)


# ======================================================
# PROGRAMA PRINCIPAL
# ======================================================
if __name__ == "__main__":
    root = tk.Tk()
    app = AppPacientes(root)
    root.mainloop()
