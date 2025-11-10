import csv
import os

NOMBRE_ARCHIVO = "datos_paises.csv"

def leer_paises():
    paises = []
    if not os.path.exists(NOMBRE_ARCHIVO):
        with open(NOMBRE_ARCHIVO, 'w', newline='', encoding='utf-8') as archivo:
            escritor = csv.DictWriter(archivo, fieldnames=["nombre", "poblacion", "superficie", "continente"])
            escritor.writeheader()
        return paises
    with open(NOMBRE_ARCHIVO, newline='', encoding='utf-8') as archivo:
        lector = csv.DictReader(archivo)
        for fila in lector:
            paises.append({
                "nombre": fila["nombre"],
                "poblacion": int(fila["poblacion"]),
                "superficie": int(fila["superficie"]),
                "continente": fila["continente"]
            })
    return paises

def guardar_paises(paises):
    with open(NOMBRE_ARCHIVO, 'w', newline='', encoding='utf-8') as archivo:
        escritor = csv.DictWriter(archivo, fieldnames=["nombre", "poblacion", "superficie", "continente"])
        escritor.writeheader()
        escritor.writerows(paises)

def agregar_pais(paises, nombre, poblacion, superficie, continente):
    if any(p["nombre"].lower() == nombre.lower() for p in paises):
        return False
    paises.append({
        "nombre": nombre,
        "poblacion": poblacion,
        "superficie": superficie,
        "continente": continente
    })
    guardar_paises(paises)
    return True

def actualizar_pais(paises, nombre, nueva_poblacion=None, nueva_superficie=None):
    for pais in paises:
        if pais["nombre"].lower() == nombre.lower():
            if nueva_poblacion is not None:
                pais["poblacion"] = nueva_poblacion
            if nueva_superficie is not None:
                pais["superficie"] = nueva_superficie
            guardar_paises(paises)
            return True
    return False

def buscar_pais(paises, nombre):
    return [p for p in paises if nombre.lower() in p["nombre"].lower()]

def filtrar_por_continente(paises, continente):
    return [p for p in paises if p["continente"].lower() == continente.lower()]

def filtrar_por_poblacion(paises, min_pob, max_pob):
    return [p for p in paises if min_pob <= p["poblacion"] <= max_pob]

def filtrar_por_superficie(paises, min_sup, max_sup):
    return [p for p in paises if min_sup <= p["superficie"] <= max_sup]

def ordenar_paises(paises, clave, descendente=False):
    return sorted(paises, key=lambda x: x[clave], reverse=descendente)

def estadisticas(paises):
    if not paises:
        return None
    max_pob = max(paises, key=lambda p: p["poblacion"])
    min_pob = min(paises, key=lambda p: p["poblacion"])
    prom_pob = sum(p["poblacion"] for p in paises) / len(paises)
    prom_sup = sum(p["superficie"] for p in paises) / len(paises)
    cont_por_cont = {}
    for p in paises:
        cont_por_cont[p["continente"]] = cont_por_cont.get(p["continente"], 0) + 1
    return {
        "mayor_poblacion": max_pob,
        "menor_poblacion": min_pob,
        "promedio_poblacion": prom_pob,
        "promedio_superficie": prom_sup,
        "paises_por_continente": cont_por_cont
    }

def mostrar_pais(p):
    return f"{p['nombre'].upper()} | Población: {p['poblacion']} | Superficie: {p['superficie']} | Continente: {p['continente'].capitalize()}"
