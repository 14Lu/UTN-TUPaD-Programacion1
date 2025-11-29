"""
Guardar los productos actualizados: Después de haber leído, buscado o agregado
productos, sobrescribir el archivo productos.txt escribiendo nuevamente todos los
productos actualizados desde la lista.
"""

def leer_productos():
    productos = []
    with open('./unidad_8/productos.txt', 'r') as file:
        for line in file:
            producto, precio, cantidad = line.strip().split(',')
            productos.append({'nombre': producto, 'precio': precio, 'cantidad': cantidad})
    return productos

def buscar_producto(productos, nombre_producto):
    for producto in productos:
        if producto['nombre'].lower() == nombre_producto.lower():
            return producto
    return None

def guardar_productos(productos):
    with open('./unidad_8/productos.txt', 'w') as file:
        for producto in productos:
            file.write(f'{producto["nombre"]},{producto["precio"]},{producto["cantidad"]}\n')

def agregar_producto(productos):
    nombre = input('Ingrese el nombre del producto: ')
    precio = input('Ingrese el precio del producto: ')
    cantidad = input('Ingrese la cantidad del producto: ')
    productos.append({'nombre': nombre, 'precio': precio, 'cantidad': cantidad})
    return productos

productos = leer_productos()
print(productos)

producto = buscar_producto(productos, 'Lapicera')
print(producto)

producto = agregar_producto(productos)
guardar_productos(productos)