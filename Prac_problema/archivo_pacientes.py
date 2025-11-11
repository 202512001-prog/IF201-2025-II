from paciente import Paciente

class Archivo:
    def __init__(self, nombre):
        self.nombre_archivo = nombre
        self.arreglo = []

    def abrir(self):
        with open(self.nombre_archivo, 'r', encoding='utf-8') as archivo:
            for linea in archivo:
                partes = linea.strip().split(';')
                paciente = Paciente(*partes)  # equivale a pasar cada campo como parámetro
                self.arreglo.append(paciente)

    def mostrar(self):
        return self.arreglo

    def __str__(self):
        salida = ""
        for pac in self.arreglo:
            salida += str(pac) + "\n"
        return salida

# -----------------------------------------------------
# Ejecución directa (para probar desde consola)
# -----------------------------------------------------
if __name__ == '__main__':
    oArch = Archivo('pacientes.txt')
    oArch.abrir()  # abre y carga los pacientes
    print(oArch)


# -----------------------------------------------------
# archivo_pacientes.py
# Gestión de archivos de pacientes (solo lectura)
# -----------------------------------------------------

from paciente import Paciente  # Importamos la clase Paciente

class Archivo:
    def __init__(self, nombre):
        """Inicializa el archivo con su nombre y crea un arreglo vacío."""
        self.nombre_archivo = nombre
        self.arreglo = []

    def abrir(self):
        """Abre el archivo, lee su contenido y crea objetos Paciente."""
        try:
            with open(self.nombre_archivo, 'r', encoding='utf-8') as archivo:
                for linea in archivo:
                    partes = linea.strip().split(';')  # separa cada dato por punto y coma
                    if len(partes) == 6:  # aseguramos que haya 6 datos
                        paciente = Paciente(partes[0], partes[1], partes[2],partes[3], partes[4], partes[5])
                        self.arreglo.append(paciente)
        except FileNotFoundError:
            print(f"Error: No se encontró el archivo {self.nombre_archivo}")

    def mostrar(self):
        """Devuelve la lista de pacientes (arreglo)."""
        return self.arreglo

    def __str__(self):
        """Devuelve una cadena con todos los pacientes (para imprimir)."""
        salida = "ID   NOMBRE              EDAD  DIAGNÓSTICO        ESPECIALIDAD        COSTO\n"
        salida += "-" * 75 + "\n"
        for p in self.arreglo:
            salida += str(p) + "\n"
        return salida

# -----------------------------------------------------
# Ejecución directa (para probar desde consola)
# -----------------------------------------------------
if __name__ == '__main__':
    oArch = Archivo('pacientes.txt')
    oArch.abrir()  # abre y carga los pacientes
    print(oArch)   # imprime todo el contenido del archivo
