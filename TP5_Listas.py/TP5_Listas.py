#Ejercicio1
notas= [7, 5, 9, 10, 5, 8, 6, 7, 9, 10]
print("Notas de los estudiantes: ", notas)
promedio = sum(notas) / len(notas)
print("Promedio de notas: ", promedio)
print("Nota mas alta: ", max(notas))
print("Nota mas baja: ", min(notas))

#Ejercicio2
productos = [ ]
for i in range(5):
    prod = input(f"Ingrese el producto {i+1}: ")
    productos.append(prod)
    print("Lista ordenada:", sorted(productos))
    eliminar = input("Ingrese el producto que desea eliminar:")
    if eliminar in productos:
        productos.remove(eliminar)
        print("Lista actualizada:", productos)
    else:
        print("El producto no esta en la lista.")

 #Ejercicio3
        import random
    numeros = [random.radint(1, 100) for _ in range(15)]
print("Lista completa:", numeros)
pares = [n for n in numeros if n % 2 == 0]
impares = [n for n in numeros if n % 2 != 0]
print("Lista de pares:", pares, "Cantidad", len(pares))
print("Lista de impares:", impares, "Cantidad:", len(impares))

#Ejercicio4
datos = [1, 3, 5, 8, 1, 9, 5, 5]
sin_repetitivos = list(set(datos))
print("Lista sin repetidos:", sin_repetitivos)

#Ejercicio5
estudiantes = ["Magali, Victor, Adelina, Ariel, Alejandra, Daniel, Francesca, Thian"]
accion = input("¿Desea agregar o eliminar un estudiante? (agregar/eliminar): ")
if accion == "agregar":
    nuevo = input("Ingrese el nombre del nuevo estudiante: ")
    estudiantes.append(nuevo)
elif accion == "Eliminar":
    borrar = input("Ingrese el nombre del estudiante a eliminar: ")
    if borrar in estudiantes:
        estudiantes.remove(borrar)
    else:
        print("Ese estudiante no esta en la lista.")
        print("Lista final:", estudiantes)

 #Ejercicio6
numeros = [200, 300, 400, 500, 600, 700, 800, 900]
ultimo = numeros.pop()
numeros.insert(0, ultimo)
print("Lista rotada:", numeros)

#Ejercicio7
temperaturas = [
[12, 20],
[15, 25],
[10, 18],
[14, 27],
[13, 22],
[11, 19],
[16, 28]
]
minimas = [t[0] for t in temperaturas]
maximas = [t[1] for t in temperaturas]
prom_min = sum(minimas) / len(minimas)
prom_max = sum(maximas) / len(maximas)
amplitudes = [t[1] - t[0] for t in temperaturas]
dia_max_amp = amplitudes.index(max(amplitudes)) + 1
print("Promedio minimas:", prom_min)
print("Promedio maximas:", prom_max)
print("Dia con mayor amplitud:", dia_max_amp)

#Ejercicio8
notas = [
    [8, 8, 9],
    [5, 6, 10],
    [8, 10, 2],
    [6, 8, 9],
    [2, 5, 8]
]
for i, fila in enumerate(notas, star=1):
    prom_est = sum(fila) / len(fila)
    print(f"Promedio del estudiante {i}: {prom_est}")
    for j in range(3):
        columna = [notas[i][j] for i in range(5)]
        prom_mat = sum(columna) / len(columna)
        print(f"Promedio de la materia {j+1}: {prom_mat}")

#Ejercicio9
tablero = [["_" for _ in range(3)] for _ in range(3)]
def mostrar_tablero(t):
    for fila in t:
        print(" ". join(fila))
        print()
        mostrar_tablero(tablero)
        fila, col = map(int, input("Jugador X, ingrese fila y columna (o-2): ").split())
        tablero[fila][col] = "X"
        mostrar_tablero(tablero)
        fila, col = map(int, input("Jugador X, ingrese fila y columna (0-2): ").split())
        tablero[fila][col] = "O"
        mostrar_tablero(tablero)

#Ejercicio10
ventas = [
    [5, 3, 2, 4, 6, 3, 2],
    [1, 4, 3, 2, 5, 6, 4],
    [3, 2, 4, 1, 2, 3, 5],
    [6, 5, 3, 4, 7, 6, 8]
    ]
for i, fila in enumerate(ventas, star=1):
    total_prod = sum(fila)
    print(f"Total del producto {i}: {total_prod}")
    totales_dias = [sum(ventas[i][j] for i in range(4)) for j in range(7)]
    dia_max = totales_dias.index(max(totales_dias)) + 1
    print("Dia con mayores ventas:", dia_max)
    totales_productos = [sum(fila) for fila in ventas]
    prod_max = totales_dias.index(max(totales_productos)) + 1
    print("Producto mas vendido:", prod_max)
    