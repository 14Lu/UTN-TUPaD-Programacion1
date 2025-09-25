tot_par = 0
tot_impar = 0
tot_neg = 0
tot_pos = 0
for n in range (0, 100):
    num5 = int(input("Ingrese un numero entero: "))
    if num5 % 2 == 0:
        tot_par += 1
        if num5 > 0:
            tot_pos += 1
        else:
            tot_neg +=1