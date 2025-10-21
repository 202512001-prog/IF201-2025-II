class Producto:
    def __init__(self, codigo: int, nombre: str, precio: float, stock: float):
        self.codigo = codigo
        self.nombre = nombre
        self.precio = precio
        self.stock = stock
        
    def __str__(self):
        return f"{self.codigo} - {self.nombre} | S/ {self.precio:.2f} | Stock: {self.stock} | Sub total: {self.sub_total()} "
    
    def sub_total(self):
        return self.precio * self.stock
    
productos = [ Producto('PO1', 'Mouse', 45.0, 10),
              Producto("P02", "Teclado", 70.0, 5), 
              Producto("P03", "Monitor", 580.0, 2)
            ]

# for p in productos:
    # print(p)  # ->  p.sub_total(): cuando no has puesto en def __str__(self):     Sub total: {self.sub_total()}
 
gran_total = 0
for p in productos:
    gran_total += p.sub_total()
    print(p)
    
print(f'Gran total: {gran_total:.2f}')
      
def calcular_total(arreglo): # Vemos que usando un metodo, obtenemos lo mismo 
    gran_total = 0
    for p in arreglo:
        gran_total += p.sub_total()
    return gran_total

print(f'Usando el método calcular_total: {calcular_total(productos):.2f}')

def obtiene_mayor(arreglo):
    precio_mayor = 0    # Ponemos un precio inicial a 0
    nombre_mayor = ''
    
    for i in range (len(arreglo)):
          if arreglo[i].precio > precio_mayor:
              precio_mayor = arreglo[i]. precio
              nombre_mayor = arreglo[i]. nombre
    return precio_mayor, nombre_mayor

print(f'El precio mayor es {obtiene_mayor(productos)}')
print(f'El precio mayor es {obtiene_mayor(productos)[0]}')
 
 
 
 
    