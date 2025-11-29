"""
Escribí un programa que permita almacenar y consultar números telefónicos.
• Permití al usuario cargar 5 contactos con su nombre como clave y número como valor.
• Luego, pedí un nombre y mostrale el número asociado, si existe.
Ejemplo:
contactos = {"Juan": "123456", "Ana": "987654"}
"""

def cargar_contactos():
    contactos = {}
    for _ in range(5):
        nombre = input('Ingrese el nombre del contacto: ')
        numero = input(f'Ingrese el numero de {nombre}: ')
        contactos[nombre] = numero
    return contactos

def consultar_contacto(contactos):
    nombre = input('Ingrese el nombre del contacto: ')
    if nombre in contactos:
        print(f'El numero de {nombre} es {contactos[nombre]}')
    else:
        print('El contacto no existe')

contactos = cargar_contactos()
consultar_contacto(contactos)