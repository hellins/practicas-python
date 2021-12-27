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
'''
script en Python que simule el sistema de validacion de datos de una plataforma digital. Se le solicitara al usuario su nombre y contraseña mientra la informacion proporcionada no coincida con la informacion previamente registarada.
'''
import os

USER = "pepe"
PASSWORD = "vidr1o"

user = ""
password = ""

while USER != user or PASSWORD != password:
    os.system("clear")
    print("                                         kit-kot")
    user = input("Usuario: ")
    password = input("Contraseña: ")
    if USER != user or PASSWORD != password:
        print("Credenciales incorrectas")
        print("Intenta nuevamente")
        input("Presiona enter para continuar")
else:
    print(" Bienvenid@")
print("hasta luego")