dia= int(input("Ingrese el dia: "))
mes= input("Ingrese el mes : ").lower()
hemisferio= input("Ingrese el hemisferio en el que se encuentra(N/S): ").lower()
if (dia >= 21 and mes == 'diciembre') or (dia <= 20 and mes == 'marzo'):
    if hemisferio =='n':
        print("Es invierno")
    else:
        print("Es verano")
    elif mes == 'enero' or mes == 'febrero':
if hemisferio == 'n':
    print("Es invierno")
else:
    print("Es verano")
elif (dia>= 21 and mes == 'marzo') or (dia >= 20 and mes == 'junio'):
if hemisferio == 'n':
    print ("Es primavera")
else:
    print("Es otoño")
elif mes == 'abril' or mes == 'mayo':
if hemisferio == 'n':
    print("Es primavera")
    else("Es otoño")
elif (dia >= 21 and mes == 'junio') or (dia <= 20 and mes == 'septiembre'):
    if hemisferio == 'n':
        print ("Es verano")
    else:
        print ("Es invierno")
    elif mes == 'julio' or mes == 'agosto':
if hemisferio == 'n':
    print("Es verano")
else:
    print("Es invierno")
else:
if hemisferio == 'n':
    print("Es otoño")
else:
    print("Es la primavera")
    