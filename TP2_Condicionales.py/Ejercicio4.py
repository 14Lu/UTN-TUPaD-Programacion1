edad1 = int(input("Ingrese su edad: "))
if edad1 < 12:
    print("Usted es un/a niño/a")
elif edad1 >= 12 and edad1 < 18:
   print ("Usted es un/a adolescente")
elif edad1 >= 18 and edad1 < 30:
    print("Usted es un/a adulto joven")
else:
    print("Usted es un/a adulto")
