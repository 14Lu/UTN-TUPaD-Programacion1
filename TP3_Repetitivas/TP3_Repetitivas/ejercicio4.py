suma2 = 0
salir = True
while salir:
    num3 = int(input("Ingrese un numero entero: "))
    suma2 = suma2 + num3
    if num3 == 0:
       salir = False
    print(f"El total de la suma es de: {suma2}")
