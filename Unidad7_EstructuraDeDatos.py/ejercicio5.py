"""
Solicita al usuario una frase e imprime:
• Las palabras únicas (usando un set).
• Un diccionario con la cantidad de veces que aparece cada palabra.
Ejemplo:
Entrada -> "hola mundo hola"
Salida ->
    palabras_unicas: {'hola', 'mundo'}
    recuento: {'hola': 2, 'mundo': 1}
"""

def palabras_unicas(frase):
    return set(frase.split())

def recuento_palabras(frase):
    recuento = {}
    palabras = frase.split()
    for palabra in palabras:
        recuento[palabra] = palabras.count(palabra)
    return recuento

frase = input('Ingrese una frase: ')
print(palabras_unicas(frase))
print(recuento_palabras(frase))