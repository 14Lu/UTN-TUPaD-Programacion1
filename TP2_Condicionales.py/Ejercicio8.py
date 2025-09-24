nombre= input("Ingrese su nombre: ")
opcion = int(input("""Ingrese una opcion
                   1- Si quiere su nombre en mayusculas
                   2- Si quiere su nombre en minusculas
                   3- Si quiere su nombre con la primera letra mayuscula
                   :"""))
if opcion == 1:
    print(nombre.upper())
elif opcion ==2:
    print(nombre.lower())
elif opcion ==3:
    print(nombre.title())
else:
    print("Ingrese una opcion valida")
    