player1 = 10
intentos = 0
num_aleatorio = 100
while player1!= num_aleatorio:
    player1 = int(input("Ingrese un numero del 0 al 9: "))
    num_aleatorio =random.randit(0,9)
    intentos += 1
    print(f"Felicidades, el numero era {num_aleatorio} y lo adivinaste en {intentos} intentos")
    