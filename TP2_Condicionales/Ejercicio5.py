contraseña = input("Ingrese una contraseña (debe tener entre 8 y 14 caracteres): ")
if len(contraseña) >= 8 and len(contraseña) <= 14:
    print("Ha ingresado una contraseña correcta")
else:
    print("Por favor, ingrese una contraseña entre 8 y 14 caracteres")
    