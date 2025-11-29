"""
Permití ingresar los nombres de 3 alumnos, y para cada uno una tupla de 3 notas.
Luego, mostrá el promedio de cada alumno.
Ejemplo:
alumnos = {
    "Sofía": (10, 9, 8),
    "Luis": (6, 7, 7)
}
"""

def cargar_alumnos():
    alumnos = {}
    for _ in range(3):
        nombre = input('Ingrese el nombre del alumno: ')
        notas = []
        for nota_idx in range(3):
            notas.append(int(input(f'Ingrese la nota {nota_idx + 1} de {nombre}: ')))
        alumnos[nombre] = notas
    return alumnos

def calcular_promedio(notas):
    return sum(notas) / len(notas)

def mostrar_promedio_alumnos(alumnos):
    for nombre, notas in alumnos.items():
        print(f'El promedio de {nombre} es {calcular_promedio(notas)}')

alumnos = cargar_alumnos()
mostrar_promedio_alumnos(alumnos)