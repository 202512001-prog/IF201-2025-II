texto = "   curso de PYTHON avanzado  " 
print (texto.strip().title())  # Elimina espacios y convierte a título
print (texto.lower().strip())  # Convierte a minúsculas y elimina espacios
print (texto.upper().strip())  # Convierte a mayúsculas y elimina espacios
print (texto.replace("PYTHON", "Java").strip())  # Reemplaza "PYTHON" por "Java" y elimina espacios
print (texto.split())  # Divide el texto en una lista de palabras
print (texto.find("PYTHON"))  # Encuentra la posición de "PYTHON"
print (texto.count("o"))  # Cuenta cuántas veces aparece "o"
print (texto.startswith("   curso"))  # Verifica si el texto empieza con "   curso"
print (texto.endswith("avanzado  "))  # Verifica si el texto termina con "avanzado  "
