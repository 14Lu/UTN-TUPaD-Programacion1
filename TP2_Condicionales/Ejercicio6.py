from statistics import mode, median, mean
import random
numeros_aleatorios = [random.randint(1, 100) for i in range(50)]
media =  median(numeros_aleatorios)
mediana = median(numeros_aleatorios)
moda = mode(numeros_aleatorios)
if media > mediana and mediana > moda:
    print("Hay sesgo positivo")
elif media < mediana and mediana < moda:
    print("Hay sesgo negativo")
elif media  == mediana and media == moda and mediana == moda:
    print("No hay sesgo")
else:
    print("No entra en ninguna categoria")
    