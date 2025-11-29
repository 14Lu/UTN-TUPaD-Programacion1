"""
Armá un diccionario donde las claves sean nombres de productos y los valores su stock.
Permití al usuario:
• Consultar el stock de un producto ingresado.
• Agregar unidades al stock si el producto ya existe.
• Agregar un nuevo producto si no existe.
"""

stock = {
    'Producto 1': 10,
    'Producto 2': 20,
    'Producto 3': 30
}

def consultar_stock(stock):
    # NOTE: Supongo que el usuario ingresa exactamente el nombre del producto
    producto = input('Ingrese el nombre del producto: ')
    if producto in stock:
        print(f'El stock de {producto} es {stock[producto]}')
    else:
        print('El producto no existe')

def agregar_stock(stock):
    producto = input('Ingrese el nombre del producto: ')
    unidades = int(input(f'Ingrese la cantidad de unidades a agregar: '))
    stock[producto] = stock.get(producto, 0) + unidades
    return stock

def main():
    while True:
        print("""
1. Consultar stock
2. Agregar stock        
3. Salir
""")
        opcion = int(input('Ingrese la opcion: '))
        match opcion:
            case 1:
                consultar_stock(stock)
            case 2:
                agregar_stock(stock)
            case 3:
                break

main()