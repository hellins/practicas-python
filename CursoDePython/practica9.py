'''
Estructura repetitiva While
script en Python que muestra los numeros del 0 al 13 utiliozando la estructura repetitiva "mientras" While
'''

print("Programa que muestra los numeros del 0 la 13")

#contador
numero = 0

while numero <= 13:
    print(f"contador: {numero}")
    numero = numero +1
else:
    print("He terminado de contar")
print("nos vemos")
'''
script en Python que sume valores partes y multiplique valores impares mientras el usuario no ingrese un 0. se debera uitilizar la estructura repetitiva "mientras" para solicitar al usuario un numero y dependiando del numero lo suma o lo multiplica.
'''
print("Programa que suma los numero pares y multiplic los impares")
suma = 0
multiplicacion = 1
numero = -1
while numero != 0:
    numero = int(input("Ingresa un numero (0 para salir)"))
    if numero % 2 == 0:
        suma = suma + numero
    else:
        multiplicacion = multiplicacion * numero
    print(f"La suma: {suma}")
    print(f"multiplicacion: {multiplicacion}")
print("no vemos")