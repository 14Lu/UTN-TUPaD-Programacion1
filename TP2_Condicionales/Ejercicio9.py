terremoto = int(input("Ingrese la magnitud del terremoto: "))
if terremoto < 3:
print("'muy leve'(imperceptible)")
elif terremoto == 3:
print("'Leve'(ligeramente perceptible)")
elif terremoto == 4:
print("'Moderado' (sentido por personas, pero generalmente no causa daños)")
elif terremoto == 6:
print("'Muy fuerte' (puede causar daños significativos)")
else:
print("'Extremo' (puede causar graves daños a gran escala)")

