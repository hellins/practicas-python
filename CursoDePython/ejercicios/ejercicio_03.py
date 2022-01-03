'''
Estructura repetitiva
script en Python
 que muestre la tabla de multiplicar de un numero ingrasado por el usuario, El usuario tambien poadra ingresar has que valor llegara la tabla.
'''

tabla = int(input("¿De que numero deas ver la tabla de multiplicar?: "))
limite = int(input("¿Hasdta quer multiplo deseas ver?: "))

print(f"                    Tabla de Multiplicar del {tabla} hasta el {limite}")

for multiplo in range(1, limite+1):
    print(f"{tabla} x {multiplo} = {tabla*multiplo}")
print("hasta luego")

# script que muestre las tablas de mu8ltiplicar de los numeros del 1 al 10. Cada tabla se muestra has el dicimo multiplo.

import os
for tabla in range(1, 11):
    os.system("clear")
    print(f"                                   Tabla de Multiplicar {tabla}")
    for multiplo in range (1,11):
        print(f"{tabla} x {multiplo} = {tabla*multiplo}")
    input("Presiona Enter para continuar........")
        
print("Hasta  luego......")