# ------------------------------------------------------------
# 📘 FUNCIONES Y MÉTODOS DE CADENA EN PYTHON
# ------------------------------------------------------------
# Las cadenas (str) en Python son inmutables, pero cuentan con
# métodos integrados que devuelven nuevas versiones modificadas.

# ------------------------------------------------------------
# 1. MÉTODOS DE CONVERSIÓN DE MAYÚSCULAS Y MINÚSCULAS
# ------------------------------------------------------------
# upper()      → Convierte todo a mayúsculas
#    'python'.upper() → 'PYTHON'
# lower()      → Convierte todo a minúsculas
#    'PyThOn'.lower() → 'python'
# capitalize() → Primera letra en mayúscula
#    'hola mundo'.capitalize() → 'Hola mundo'
# title()      → Mayúsculas al inicio de cada palabra
#    'curso de python'.title() → 'Curso De Python'
# swapcase()   → Invierte mayúsculas y minúsculas
#    'PyThOn'.swapcase() → 'pYtHoN'

# ------------------------------------------------------------
# 2. MÉTODOS DE ELIMINACIÓN DE ESPACIOS O CARACTERES
# ------------------------------------------------------------
# strip()  → Elimina espacios al inicio y final
#    ' hola '.strip() → 'hola'
# lstrip() → Elimina espacios al inicio
#    ' hola'.lstrip() → 'hola'
# rstrip() → Elimina espacios al final
#    'hola '.rstrip() → 'hola'
# También puedes eliminar caracteres específicos:
#    '---texto---'.strip('-') → 'texto'

# ------------------------------------------------------------
# 3. MÉTODOS DE BÚSQUEDA Y POSICIÓN
# ------------------------------------------------------------
# find(sub)    → Devuelve posición de la subcadena o -1 si no existe
#    'programacion'.find('gra') → 3
# rfind(sub)   → Busca desde el final
#    'banana'.rfind('a') → 5
# index(sub)   → Igual que find(), pero lanza error si no existe
#    'hola'.index('o') → 1
# count(sub)   → Cuenta cuántas veces aparece una subcadena
#    'banana'.count('a') → 3
# startswith() → Verifica si empieza con algo
#    'python'.startswith('py') → True
# endswith()   → Verifica si termina con algo
#    'hola.py'.endswith('.py') → True

# ------------------------------------------------------------
# 4. MÉTODOS DE REEMPLAZO Y DIVISIÓN
# ------------------------------------------------------------
# replace(viejo, nuevo) → Reemplaza subcadenas
#    'hola mundo'.replace('mundo','Python') → 'hola Python'
# split(sep)            → Divide en lista por separador
#    'uno,dos,tres'.split(',') → ['uno', 'dos', 'tres']
# rsplit(sep, n)        → Divide desde el final
#    'a-b-c-d'.rsplit('-', 1) → ['a-b-c', 'd']
# splitlines()          → Divide por saltos de línea
#    "uno\ndos\ntres".splitlines() → ['uno','dos','tres']
# join(lista)           → Une una lista de cadenas con un separador
#    '-'.join(['A','B','C']) → 'A-B-C'

# ------------------------------------------------------------
# 5. MÉTODOS DE FORMATO Y ALINEACIÓN
# ------------------------------------------------------------
# center(n, char) → Centra la cadena con relleno
#    'py'.center(6, '*') → '**py**'
# ljust(n, char)  → Alinea a la izquierda
#    'py'.ljust(6, '-') → 'py----'
# rjust(n, char)  → Alinea a la derecha
#    'py'.rjust(6, '-') → '----py'
# zfill(n)        → Rellena con ceros a la izquierda
#    '42'.zfill(5) → '00042'
# format()        → Inserta valores en texto
#    'Precio: {:.2f}'.format(25.5) → 'Precio: 25.50'
# f-strings       → Nueva forma más legible
#    f"Precio: {25.5:.2f}" → 'Precio: 25.50'

# ------------------------------------------------------------
# 6. MÉTODOS DE COMPROBACIÓN (RETORNAN TRUE O FALSE)
# ------------------------------------------------------------
# isalnum()  → Solo letras y números
#    'abc123'.isalnum() → True
# isalpha()  → Solo letras
#    'abc'.isalpha() → True
# isdigit()  → Solo dígitos
#    '123'.isdigit() → True
# isdecimal()→ Solo números decimales
#    '123'.isdecimal() → True
# isnumeric()→ Cifras numéricas (romanos, fracciones)
#    'Ⅳ'.isnumeric() → True
# islower()  → Todas en minúsculas
#    'python'.islower() → True
# isupper()  → Todas en mayúsculas
#    'PYTHON'.isupper() → True
# istitle()  → Cada palabra inicia con mayúscula
#    'Hola Mundo'.istitle() → True
# isspace()  → Solo espacios
#    ' '.isspace() → True
# isascii()  → Todos los caracteres ASCII
#    'texto'.isascii() → True

# ------------------------------------------------------------
# 7. MÉTODOS DE TRADUCCIÓN Y CODIFICACIÓN
# ------------------------------------------------------------
# maketrans() + translate() → Sustituye caracteres según tabla
#    'hola'.translate(str.maketrans('ho','HO')) → 'HOla'
# encode() → Codifica a bytes
#    'áéí'.encode('utf-8')
# decode() → Decodifica bytes a texto
#    b'\xc3\xa1'.decode('utf-8') → 'á'

# ------------------------------------------------------------
# 🧩 EJEMPLO INTEGRADO
# ------------------------------------------------------------
# texto = " curso de PYTHON avanzado "
# print(texto.strip().title())         # "Curso De Python Avanzado"
# print(texto.lower().count("python")) # 1
# print(texto.replace("avanzado", "básico"))  # " curso de PYTHON básico "
# print("python".center(20, "*"))      # "*******python*******"
# print("abc123".isalnum())            # True

# ------------------------------------------------------------
# 🧭 RESUMEN PRÁCTICO
# ------------------------------------------------------------
# Tipo de Función          → Ejemplos de Métodos
# ------------------------------------------------------------
# Conversión               → upper, lower, title, capitalize, swapcase
# Eliminación              → strip, lstrip, rstrip
# Búsqueda                 → find, count, startswith, endswith
# Reemplazo/División       → replace, split, join
# Formato                  → center, ljust, rjust, zfill, format, f-string
# Validación               → isalpha, isdigit, islower, isupper, isspace
# Codificación/Traducción  → encode, decode, translate
# ------------------------------------------------------------