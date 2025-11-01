import csv
import os

# ---------- FUNCIONES AUXILIARES ----------

def normalizar_titulo(titulo):
    """Normaliza el título eliminando espacios y pasando a mayúsculas."""
    return titulo.strip().upper()

def cargar_catalogo():
    """Carga el catálogo desde catalogo.csv o crea uno vacío."""
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
    """Guarda el catálogo actual en catalogo.csv."""
    with open("catalogo.csv", "w", newline="", encoding="utf-8") as archivo:
        campos = ["TITULO", "CANTIDAD"]
        escritor = csv.DictWriter(archivo, fieldnames=campos)
        escritor.writeheader()
        escritor.writerows(catalogo)

def buscar_titulo(catalogo, titulo):
    """Devuelve el índice del título si existe, o -1 si no."""
    for i, libro in enumerate(catalogo):
        if normalizar_titulo(libro["TITULO"]) == normalizar_titulo(titulo):
            return i
    return -1

# ---------- FUNCIONES DEL MENÚ ----------

def ingresar_titulos(catalogo):
    """Permite ingresar varios títulos nuevos."""
    while True:
        titulo = input("Ingrese título (ENTER para salir): ").strip()
        if titulo == "":
            break
        if buscar_titulo(catalogo, titulo) != -1:
            print("⚠️ Ese título ya existe. Ingrese otro.")
        else:
            cantidad = input("Ingrese cantidad de ejemplares: ")
            if cantidad.isdigit():
                catalogo.append({
                    "TITULO": normalizar_titulo(titulo),
                    "CANTIDAD": int(cantidad)
                })
                guardar_catalogo(catalogo)
                print("✅ Título agregado correctamente.")
            else:
                print("⚠️ Ingrese solo números en la cantidad.")

def ingresar_ejemplares(catalogo):
    """Agrega ejemplares a un título existente."""
    titulo = input("Ingrese título existente: ")
    indice = buscar_titulo(catalogo, titulo)
    if indice == -1:
        print("⚠️ Título no encontrado.")
    else:
        cantidad = input("Ingrese cantidad a agregar: ")
        if cantidad.isdigit():
            catalogo[indice]["CANTIDAD"] += int(cantidad)
            guardar_catalogo(catalogo)
            print("✅ Ejemplares agregados correctamente.")
        else:
            print("⚠️ Ingrese solo números.")

def mostrar_catalogo(catalogo):
    """Muestra todo el catálogo en pantalla."""
    print("\n📚 --- CATÁLOGO ACTUAL --- 📚")
    if len(catalogo) == 0:
        print("No hay libros cargados todavía.")
    else:
        for libro in catalogo:
            print(f"- {libro['TITULO']}: {libro['CANTIDAD']} ejemplares")
    print("-----------------------------\n")

def consultar_disponibilidad(catalogo):
    """Consulta cuántos ejemplares hay de un título."""
    titulo = input("Ingrese el título: ")
    indice = buscar_titulo(catalogo, titulo)
    if indice == -1:
        print("⚠️ Ese título no está en el catálogo.")
    else:
        cant = catalogo[indice]["CANTIDAD"]
        print(f"El libro '{catalogo[indice]['TITULO']}' tiene {cant} ejemplares disponibles.")

def listar_agotados(catalogo):
    """Muestra los libros con 0 ejemplares."""
    print("\n📕 --- LIBROS AGOTADOS ---")
    agotados = [libro for libro in catalogo if libro["CANTIDAD"] == 0]
    if agotados:
        for libro in agotados:
            print(f"- {libro['TITULO']}")
    else:
        print("No hay libros agotados.")
    print("----------------------------\n")

def actualizar_ejemplares(catalogo):
    """Permite registrar un préstamo o devolución."""
    titulo = input("Ingrese título: ")
    indice = buscar_titulo(catalogo, titulo)
    if indice == -1:
        print("⚠️ Título no encontrado.")
        return

    print("1. Préstamo (resta ejemplares)")
    print("2. Devolución (suma ejemplares)")
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

# ---------- MENÚ PRINCIPAL ----------

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
6. Actualizar ejemplares (préstamo/devolución)
7. Salir
=============================
""")
        opc = input("Seleccione una opción: ")

        match opc:
            case "1": ingresar_titulos(catalogo)
            case "2": ingresar_ejemplares(catalogo)
            case "3": mostrar_catalogo(catalogo)
            case "4": consultar_disponibilidad(catalogo)
            case "5": listar_agotados(catalogo)
            case "6": actualizar_ejemplares(catalogo)
            case "7":
                print("👋 Programa finalizado.")
                break
            case _: print("⚠️ Opción inválida. Intente de nuevo.")

# ---------- PUNTO DE ENTRADA ----------
if __name__ == "__main__":
    menu()
