"""
Leer y mostrar productos: Crear un programa que abra productos.txt, lea cada
línea, la procese con .strip() y .split(","), y muestre los productos en el siguiente
formato:
Producto: Lapicera | Precio: $120.5 | Cantidad: 30
"""

with open('./unidad_8/productos.txt', 'r') as file:
    for line in file:
        producto, precio, cantidad = line.strip().split(',')
        print(f'Producto: {producto} | Precio: ${precio} | Cantidad: {cantidad}')