'''
Estructura repetitiva
script en Python que muestre los numeros enteros desde 0 hasta el 13 usando un ciclo For.
'''

print("Programa que muestra los numeros desde el 0 hasta el 13")
for numero in range(14):
    print(f"{numero}")
    
print("hasta luego")
'''
script en Python que imprima los numeros pares desde el 2 hasta el 20 haciendo uso del ciclo for.
'''
print("Programa que muestra los numeros pares desde el 2 hasta el 20 ")

for numero in range(2,21,2):
    print(f"{numero}")
    
print("hasta luego")

# Metodo 2

print("      Metodo 2")

for numero in range(1,11):
    print(f"par: {numero*2}")
    
print("Hasta luego")

print("*"*20)

#  Metodo 3

print(" Metodo 3")

for numero in range(2,21):
    if numero % 2 == 0:
        print(f"par: {numero}")
        
print("Hasta luego")

import os
import time

for numero in range(10, -1, -1):
    os.system("clear")
    print(numero)
    time.sleep(1)
else:
    print("Feliz Año")
    
print("  Hasta luego")