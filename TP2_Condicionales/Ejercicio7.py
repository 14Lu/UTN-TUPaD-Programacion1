frase = input("Ingrese una frase: ")
VOCALES = [ 'a', 'e','i','o','u','A','E','I','O','U']
if frase [-1] in VOCALES:
    print(f"{frase}!")
else:
    print(frase)
