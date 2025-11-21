"""
Crea una función recursiva que calcule la potencia de un número base elevado a un
exponente, utilizando la fórmula n^m = n * n^(m-1)
Prueba esta función en un algoritmo general.
"""

def potencia(base, exponente):
    if exponente == 0:
        return 1
    else:
        return base * potencia(base, exponente - 1)


b = int(input("Base: "))
e = int(input("Exponente: "))
print(f"{b}^{e} = {potencia(b, e)}")