"""
Dado dos sets de números, representando dos listas de estudiantes que aprobaron Parcial 1
y Parcial 2:
• Mostrá los que aprobaron ambos parciales.
• Mostrá los que aprobaron solo uno de los dos.
• Mostrá la lista total de estudiantes que aprobaron al menos un parcial (sin repetir).
"""

parcial_1 = {1, 2, 3, 4, 5}
parcial_2 = {4, 5, 6, 7, 8}

print('Los que aprobaron ambos parciales:', parcial_1.intersection(parcial_2))
print('Los que aprobaron solo uno de los dos:', parcial_1.symmetric_difference(parcial_2))
print('La lista total de estudiantes que aprobaron al menos un parcial:', parcial_1.union(parcial_2))