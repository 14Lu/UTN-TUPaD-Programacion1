import csv
import os

def normalizar_titulo(titulo):
    """Elimina espacios y convierte a mayúsculas."""
    return titulo.strip().upper()

def cargar_catalogo():
    """Carga catálogo desde CSV o devuelve lista vacía si no existe."""
    catalogo = []
    if os.path.exists("catalogo.csv"):
        with open("catalogo.csv", newline="", encoding="utf-8") as archivo:
            lector = csv.DictReader(archivo)
            for fila in lector:
                catalogo.append({
                    "TITULO": fila["TITULO"],
                    "CANTIDAD": int(fila["CANTIDAD"])
                })
    return catalogo

def guardar_catalogo(catalogo):
    """Guarda el catálogo en CSV."""
    with open("catalogo.csv", "w", newline="", encoding="utf-8") as archivo:
        campos = ["TITULO", "CANTIDAD"]
        escritor = csv.DictWriter(archivo, fieldnames=campos)
        escritor.writeheader()
        escritor.writerows(catalogo)

def buscar_titulo(catalogo, titulo):
    """Devuelve el índice del título si existe o -1 si no."""
    for i, libro in enumerate(catalogo):
        if normalizar_titulo(libro["TITULO"]) == normalizar_titulo(titulo):
            return i
    return -1
def ingresar_titulos_multiples(catalogo):
    while True:
        cantidad_total = input("¿Cuántos libros desea ingresar?: ")
        if cantidad_total.isdigit():
            cantidad_total = int(cantidad_total)
            break
        else:
            print("⚠️ Ingrese solo números.")

    for i in range(cantidad_total):
        print(f"\nLibro {i+1} de {cantidad_total}")
        titulo = input("Ingrese título: ").strip()
        if titulo == "":
            print("⚠️ El título no puede estar vacío.")
            continue
        if buscar_titulo(catalogo, titulo) != -1:
            print("⚠️ Ese título ya existe, se omite.")
            continue
        cantidad = input("Ingrese cantidad de ejemplares: ")
        if cantidad.isdigit() and int(cantidad) >= 0:
            catalogo.append({
                "TITULO": normalizar_titulo(titulo),
                "CANTIDAD": int(cantidad)
            })
        else:
            print("⚠️ Cantidad inválida. Se omite este libro.")

    guardar_catalogo(catalogo)
    print("\n✅ Libros cargados correctamente.\n")
def ingresar_ejemplares(catalogo):
    titulo = input("Ingrese título existente: ")
    indice = buscar_titulo(catalogo, titulo)
    if indice == -1:
        print("⚠️ Título no encontrado.")
        return
    cantidad = input("Ingrese cantidad a agregar: ")
    if cantidad.isdigit():
        catalogo[indice]["CANTIDAD"] += int(cantidad)
        guardar_catalogo(catalogo)
        print("✅ Ejemplares agregados correctamente.")
    else:
        print("⚠️ Ingrese solo números.")
def mostrar_catalogo(catalogo):
    print("\n📚 --- CATÁLOGO ACTUAL --- 📚")
    if len(catalogo) == 0:
        print("No hay libros cargados todavía.")
    else:
        print(f"{'TÍTULO':<40} | {'CANTIDAD':>8}")
        print("-" * 52)
        for libro in catalogo:
            print(f"{libro['TITULO']:<40} | {libro['CANTIDAD']:>8}")
    print("-----------------------------\n")
def consultar_disponibilidad(catalogo):
    titulo = input("Ingrese el título a consultar: ")
    indice = buscar_titulo(catalogo, titulo)
    if indice == -1:
        print("⚠️ Ese título no está en el catálogo.")
    else:
        cant = catalogo[indice]["CANTIDAD"]
        print(f"El libro '{catalogo[indice]['TITULO']}' tiene {cant} ejemplares disponibles.")
def listar_agotados(catalogo):
    print("\n📕 --- LIBROS AGOTADOS ---")
    agotados = [libro for libro in catalogo if libro["CANTIDAD"] == 0]
    if agotados:
        for libro in agotados:
            print(f"- {libro['TITULO']}")
    else:
        print("No hay libros agotados.")
    print("----------------------------\n")
def agregar_titulo_individual(catalogo):
    titulo = input("Ingrese nuevo título: ").strip()
    if titulo == "":
        print("⚠️ El título no puede estar vacío.")
        return
    if buscar_titulo(catalogo, titulo) != -1:
        print("⚠️ Ese título ya existe.")
        return
    cantidad = input("Ingrese cantidad inicial: ")
    if cantidad.isdigit() and int(cantidad) >= 0:
        catalogo.append({
            "TITULO": normalizar_titulo(titulo),
            "CANTIDAD": int(cantidad)
        })
        guardar_catalogo(catalogo)
        print("✅ Título agregado correctamente.")
    else:
        print("⚠️ Cantidad inválida.")
def actualizar_ejemplares(catalogo):
    titulo = input("Ingrese título: ")
    indice = buscar_titulo(catalogo, titulo)
    if indice == -1:
        print("⚠️ Título no encontrado.")
        return

    print("1. Préstamo (resta 1 si hay ejemplares)")
    print("2. Devolución (suma 1)")
    opcion = input("Seleccione una opción: ")

    if opcion == "1":
        if catalogo[indice]["CANTIDAD"] > 0:
            catalogo[indice]["CANTIDAD"] -= 1
            guardar_catalogo(catalogo)
            print("📘 Préstamo registrado.")
        else:
            print("⚠️ No hay ejemplares disponibles.")
    elif opcion == "2":
        catalogo[indice]["CANTIDAD"] += 1
        guardar_catalogo(catalogo)
        print("📗 Devolución registrada.")
    else:
        print("⚠️ Opción no válida.")
def menu():
    catalogo = cargar_catalogo()

    while True:
        print("""
====== MENÚ BIBLIOTECA ======
1. Ingresar títulos (múltiples)
2. Ingresar ejemplares
3. Mostrar catálogo
4. Consultar disponibilidad
5. Listar agotados
6. Agregar título individual
7. Actualizar ejemplares (préstamo/devolución)
8. Salir
=============================
""")
        opc = input("Seleccione una opción: ")

        match opc:
            case "1": ingresar_titulos_multiples(catalogo)
            case "2": ingresar_ejemplares(catalogo)
            case "3": mostrar_catalogo(catalogo)
            case "4": consultar_disponibilidad(catalogo)
            case "5": listar_agotados(catalogo)
            case "6": agregar_titulo_individual(catalogo)
            case "7": actualizar_ejemplares(catalogo)
            case "8":
                print("👋 Programa finalizado.")
                break
            case _:
                print("⚠️ Opción inválida. Intente de nuevo.")
if __name__ == "__main__":
    menu()

