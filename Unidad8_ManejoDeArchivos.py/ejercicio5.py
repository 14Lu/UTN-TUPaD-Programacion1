"""
Buscar producto por nombre: Pedir al usuario que ingrese el nombre de un
producto. Recorrer la lista de productos y, si lo encuentra, mostrar todos sus datos. Si
no existe, mostrar un mensaje de error.
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


productos = leer_productos()
nombre_producto = input('Ingrese el nombre del producto: ')
producto = buscar_producto(productos, nombre_producto)

if producto:
    print(producto)
else:
    print('El producto no existe')