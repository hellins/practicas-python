'''
Estructura Repetitiva
script en Python que muestre uno a uno los simbolos de una palabra o frase. por ejemplo si la frase fuera "Hola" se deberia imprimir
H
o
l
a
'''
frase = input("Ingresa una frase o palabra: ")
print("Los sombolos de tu frase/palabra son: ")

for simbolo in frase:
    print(f"{simbolo}")
    
print("Hasta luego...")

'''
script en Python que pregunte al usuario una cantidad de numeros a registar, le solicite dichos valores y finalmente imprima el pŕomedio de los mismos.
'''

acumulador = 0
print("Vamos a calcular un promedio")
total_datos = int(input("¿Cuantos datos deseas registar? "))

for valor in range(total_datos):
    numero = int(input(f"Ingresa el valor {valor+1}:"))
    acumulador += numero
    
promedio = acumulador / total_datos
print(f"El promedio es: {promedio}")