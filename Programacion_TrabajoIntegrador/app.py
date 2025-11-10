# Importa todas las funciones del archivo gestor_datos_paises.py
from gestor_datos_paises import *

# Funcion principal que maneja el menu del programa
def menu():
    # Carga los paises desde el archivo CSV
    paises = leer_paises()

    while True:
        # Menú principal
        print("\n=== GESTION DE DATOS DE PAISES ===")
        print("1. Agregar pais")
        print("2. Actualizar pais")
        print("3. Buscar pais")
        print("4. Filtrar paises")
        print("5. Ordenar paises")
        print("6. Mostrar estadisticas")
        print("7. Mostrar todos")
        print("8. Salir")

        # Solicita la opcion al usuario
        opcion = input("Elegí una opción: ").strip()

        # --- OPCIÓN 1: Agregar país ---
        if opcion == "1":
            nombre = input("Nombre: ").strip()
            poblacion = int(input("Población: "))
            superficie = int(input("Superficie: "))
            continente = input("Continente: ").strip()
            if agregar_pais(paises, nombre, poblacion, superficie, continente):
                print("Pais agregado correctamente.")
            else:
                print("Ese pais ya existe.")

        # --- OPCIÓN 2: Actualizar pais existente ---
        elif opcion == "2":
            nombre = input("Nombre del pais a actualizar: ")
            nueva_poblacion = input("Nueva poblacion (dejar vacio si no cambia): ").strip()
            nueva_superficie = input("Nueva superficie (dejar vacío si no cambia): ").strip()
            # Convierte los valores solo si se ingresan
            nueva_poblacion = int(nueva_poblacion) if nueva_poblacion else None
            nueva_superficie = int(nueva_superficie) if nueva_superficie else None
            if actualizar_pais(paises, nombre, nueva_poblacion, nueva_superficie):
                print("País actualizado.")
            else:
                print("No se encontró el país.")

        # --- OPCIÓN 3: Buscar pais por nombre ---
        elif opcion == "3":
            nombre = input("Buscar por nombre: ")
            resultados = buscar_pais(paises, nombre)
            if resultados:
                for p in resultados:
                    print(mostrar_pais(p))
            else:
                print("No se encontraron coincidencias.")

        # --- OPCIÓN 4: Filtros ---
        elif opcion == "4":
            print("\n1. Por continente\n2. Por rango de poblacion\n3. Por rango de superficie")
            sub = input("Elegi: ")

            # Filtrar por continente
            if sub == "1":
                cont = input("Continente: ")
                for p in filtrar_por_continente(paises, cont):
                    print(mostrar_pais(p))
            # Filtrar por rango de poblacion
            elif sub == "2":
                min_p = int(input("Población mínima: "))
                max_p = int(input("Población máxima: "))
                for p in filtrar_por_poblacion(paises, min_p, max_p):
                    print(mostrar_pais(p))
            # Filtrar por rango de superficie
            elif sub == "3":
                min_s = int(input("Superficie mínima: "))
                max_s = int(input("Superficie máxima: "))
                for p in filtrar_por_superficie(paises, min_s, max_s):
                    print(mostrar_pais(p))

        # --- OPCIÓN 5: Ordenar países ---
        elif opcion == "5":
            print("\n1. Nombre\n2. Población\n3. Superficie")
            sub = input("Elegí: ")
            # Define la clave de orden segun el numero elegido
            clave = "nombre" if sub == "1" else "poblacion" if sub == "2" else "superficie"
            # Pregunta si el orden debe ser descendente
            desc = input("¿Descendente? (s/n): ").lower() == "s"
            # Muestra la lista ordenada
            ordenados = ordenar_paises(paises, clave, desc)
            for p in ordenados:
                print(mostrar_pais(p))

        # --- OPCIÓN 6: Mostrar estadisticas ---
        elif opcion == "6":
            est = estadisticas(paises)
            if est:
                print("\nPaís con mayor poblacion:", mostrar_pais(est["mayor_poblacion"]))
                print("País con menor poblacion:", mostrar_pais(est["menor_poblacion"]))
                print(f"Promedio de poblacion: {est['promedio_poblacion']:.2f}")
                print(f"Promedio de superficie: {est['promedio_superficie']:.2f}")
                print("Cantidad de paises por continente:")
                for c, cant in est["paises_por_continente"].items():
                    print(f"  {c.capitalize()}: {cant}")
            else:
                print("No hay datos cargados.")

        # --- OPCION 7: Mostrar todos los paises cargados ---
        elif opcion == "7":
            for p in paises:
                print(mostrar_pais(p))

        # --- OPCION 8: Salir del programa ---
        elif opcion == "8":
            print("Saliendo del programa...")
            break

        # --- Cualquier otra opción ---
        else:
            print("Opción invalida. Intentá nuevamente.")
            

# Llama al menu principal al iniciar el programa
menu()
