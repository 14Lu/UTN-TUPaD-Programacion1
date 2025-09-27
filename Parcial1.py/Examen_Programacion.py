titulos = ["Harry Potter", "Lo que el viento se llevó", "El Principito"]
ejemplares = [5, 3, 4]

print("=== SISTEMA DE GESTIÓN DE LA BIBLIOTECA ===")
print("Catálogo inicial cargado con 3 títulos de ejemplo.")

while True:
    print("Menú:")
    print("1 - Ingresar títulos")
    print("2 - Ingresar ejemplares")
    print("3 - Mostrar catálogo")
    print("4 - Consultar disponibilidad")
    print("5 - Listar agotados")
    print("6 - Agregar título")
    print("7 - Actualizar ejemplares (Préstamo / Devolución)")
    print("8 - Salir")

    opcion = input("Ingrese opción (1-8): ")
    if not opcion.isdigit():
        print("Opción inválida: debe ingresar un número entre 1 y 8.")
        continue
    opcion = int(opcion)
    if opcion == 1:
        print("-- INGRESAR TÍTULOS (Enter para finalizar) --")
        while True:
            nuevo_titulo = input("Ingrese título: ").strip()
            if nuevo_titulo == "":
                print("Carga finalizada.")
                break
            if nuevo_titulo.lower() in [t.lower() for t in titulos]:
                print("Ese título ya existe. No se agregó.")
                continue
            cantidad_str = input("Ingrese cantidad de ejemplares: ").strip()
            if not cantidad_str.isdigit():
                print("Cantidad inválida.")
                continue
            cantidad = int(cantidad_str)
            titulos.append(nuevo_titulo)
            ejemplares.append(cantidad)
            print(f"'{nuevo_titulo}' agregado con {cantidad} ejemplares.")
    elif opcion == 2:
        print("-- INGRESAR EJEMPLARES --")
        busqueda = input("Ingrese título existente: ").strip()
        if busqueda.lower() not in [t.lower() for t in titulos]:
            print("Título no encontrado.")
            continue
        idx = [t.lower() for t in titulos].index(busqueda.lower())
        cantidad_str = input("Ingrese cantidad a sumar: ").strip()
        if not cantidad_str.isdigit():
            print("Cantidad inválida.")
            continue
        cantidad = int(cantidad_str)
        ejemplares[idx] += cantidad
        print(f"Se sumaron {cantidad} ejemplares a '{titulos[idx]}'. Total: {ejemplares[idx]}")

    elif opcion == 3:
        print("-- CATÁLOGO COMPLETO --")
        if len(titulos) == 0:
            print("El catálogo está vacío.")
        else:
            for i in range(len(titulos)):
                print(f"{i+1}. {titulos[i]} ({ejemplares[i]} ejemplares)")
        input("Presione Enter para volver al menú.")
    elif opcion == 4:
        print("-- CONSULTAR DISPONIBILIDAD --")
        consulta = input("Ingrese título a consultar: ").strip()
        if consulta == "":
            print("Consulta cancelada.")
            continue
        if consulta.lower() not in [t.lower() for t in titulos]:
            print("Título no encontrado.")
        else:
            idx = [t.lower() for t in titulos].index(consulta.lower())
            print(f"'{titulos[idx]}' tiene {ejemplares[idx]} ejemplares disponibles.")

    elif opcion == 5:
        print("-- TÍTULOS AGOTADOS --")
        agotados = [titulos[i] for i in range(len(titulos)) if ejemplares[i] == 0]
        if len(agotados) == 0:
            print("No hay títulos agotados.")
        else:
            for t in agotados:
                print(f"- {t}")
    elif opcion == 6:
        print("-- AGREGAR TÍTULO --")
        nuevo = input("Ingrese título nuevo: ").strip()
        if nuevo == "":
            print("Operación cancelada.")
            continue
        if nuevo.lower() in [t.lower() for t in titulos]:
            print("Ese título ya existe.")
            continue
        cantidad_str = input("Ingrese cantidad de ejemplares: ").strip()
        if not cantidad_str.isdigit():
            print("Cantidad inválida.")
            continue
        cantidad = int(cantidad_str)
        titulos.append(nuevo)
        ejemplares.append(cantidad)
        print(f"'{nuevo}' agregado con {cantidad} ejemplares.")
    elif opcion == 7:
        print("-- ACTUALIZAR EJEMPLARES --")
        nombre = input("Ingrese título: ").strip()
        if nombre.lower() not in [t.lower() for t in titulos]:
            print("Título no encontrado.")
            continue
        idx = [t.lower() for t in titulos].index(nombre.lower())
        tipo = input("Ingrese 'P' para Préstamo o 'D' para Devolución: ").strip().lower()
        if tipo not in ("p", "d"):
            print("Opción inválida.")
            continue
        cantidad_str = input("Ingrese cantidad: ").strip()
        if not cantidad_str.isdigit():
            print("Cantidad inválida.")
            continue
        cantidad = int(cantidad_str)
        if tipo == "p":
            if cantidad > ejemplares[idx]:
                print("No hay suficientes ejemplares.")
                continue
            ejemplares[idx] -= cantidad
            print(f"Préstamo registrado. Stock actual: {ejemplares[idx]}")
        else:
            ejemplares[idx] += cantidad
            print(f"Devolución registrada. Stock actual: {ejemplares[idx]}")
    elif opcion == 8:
        print("Saliendo del programa. ¡Éxitos!")
        break
    else:
        print("Opción inválida. Ingrese un número del 1 al 8.")