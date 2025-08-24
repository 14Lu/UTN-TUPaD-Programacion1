  #Ejercicio 1
print("Hola Mundo!")


  #Ejercicio 2
nombre = input ("Ingresa tu nombre: ")
print(f"Hola {nombre}!")


   #Ejercicio 3
nombre = input("Ingresa tu nombre: ")
apellido = input("Ingresa tu apellido: ")
edad = input("Ingresa tu edad: ")
lugar = input("Ingresa tu lugar de residencia: ")
print(f"Soy {nombre} {apellido}, tengo {edad} años y vivo en {lugar}. ")

    #Ejercicio 4
import math
radio = float(input("Ingresa el radio del circulo: "))
area = math.pi * radio **2
perimetro = 2 * math.pi * radio
print (f"El area es {area:.2f} y el perimetro es {perimetro: .2f}.")


   #Ejercicio 5
segundos = int (input("Ingresa la cantidad de segundos: "))
horas = segundos / 3600
print (f"{segundos} segundos equivales a {horas} horas.")

    #Ejercicio 6

numero = int(input("Ingresa un numero: "))
print("Tabla de multiplicar de ", numero)
for i in range(1,11):
    print(f"{numero} x {i} = {numero * i}")


    #Ejercicio 7
    num1 = float(input("Ingresa el primer numero(distinto de 0): "))
num2 = float(input("Ingresa el segundo numero(distinto de 0): "))

suma = num1+num2
resta = num1-num2
multiplicacion = num1*num2
division = num1/num2

print(f"Suma: {suma}")
print(f"Resta: {resta}")
print(f"Multiplicacion: {multiplicacion}")
print(f"Division: {division}")

   #Ejercicio 8
peso = float(input("Ingresa tu peso en kg: "))
altura = float(input("Ingresa tu altura en metros: "))
imc = peso/(altura**2)
print("Tu indice de masa corporal es:",imc)

   #Ejercicio 9
No me salio, no pude entender bien el punto

  #Ejercicio 10
 num1 = float(input("Ingresa el primer numero: "))
num2 = float(input("Ingresa el segundo numero: "))
num3 = float(input("Ingresa el tercer numero: "))

promedio = (num1+num2+num3) / 3
print ("El promedio de los tres numeros es :", promedio)

