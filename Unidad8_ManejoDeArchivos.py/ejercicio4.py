"""
Cargar productos en una lista de diccionarios: Al leer el archivo, cargar los datos en
una lista llamada productos, donde cada elemento sea un diccionario con claves:
nombre, precio, cantidad.
"""

productos = []

with open('./unidad_8/productos.txt', 'r') as file:
    for line in file:
        producto, precio, cantidad = line.strip().split(',')
        productos.append({'nombre': producto, 'precio': precio, 'cantidad': cantidad})

print(productos)