class Producto:
 def __init__(self, codigo, nombre, precio, stock):
    self.codigo = codigo
    self.nombre = nombre
    self.precio = precio
    self.stock = stock
 def __str__(self):
    return f"{self.codigo} - {self.nombre} | S/ {self.precio:.2f} | Stock: {self.stock} | Subtotal: {self.subtotal()}"
 def subtotal(self):
     return self.precio * self.stock
 
productos = [
 Producto("P01", "Mouse", 45.0, 10),
 Producto("P02", "Teclado", 70.0, 5),
 Producto("P03", "Monitor", 580.0, 2)
]
gran_total = 0
for p in productos:
   gran_total += p.subtotal() 
   print(p)
print(f"Gran Total: {gran_total:.2f}")

def calcula_total(arreglo):
    gran_total = 0
    for p in arreglo:
        gran_total += p.subtotal() 
    return gran_total

def obtiene_mayor(arreglo):
    precio_mayor = 0
    nombre_mayor = ""
    for i in range(len(arreglo)):
        if arreglo[i].precio > precio_mayor:
            precio_mayor = arreglo[i].precio
            nombre_mayor = arreglo[i].nombre
    return precio_mayor, nombre_mayor

print(f"Usando el metodo calcula_total: {calcula_total(productos):.2f}")
print(f"el precio mayor es {obtiene_mayor(productos)[0]}, perteneciente al producto {obtiene_mayor(productos)[1]}")
    

 
 
 
 
    