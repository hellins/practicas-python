''''
Estructura Repetitiva
script en Python que muestre un cronometro en formato de 24 horas. El despligue seguira el formato h:m:s. El cronograma debera iniciar en 0:0:0 y podra legar hasta 23:59:59. Implementar retardo de 1 segundo y limpieza de pantalla de forma tal que solo se vea  un tiempo en pantalla.
'''
'''
import time
import os

for hora in range(24):
    for minuto in range (60):
        for segundo in range(60):
            os.system("clear")
            print(f"{hora}:{minuto}:{segundo}")
            time.sleep(1)
            '''
'''
Procedimientos
script en Python que imprima un saludo en pantalla haciendo uso de un procedimiento.
'''

def saludo():
    print("Hola mundo")
    
saludo()
print("hasta luego .....")

'''
Scropt en Python solicite el nombre del usuario y lo salude de manera personalizadda haciendo uso de un procedimiento.
'''

def saludo_personalizado():
    nombre = input("Hola ¿Como te llamas: ? ")
    print(f"Gusto en conocerte, {nombre}")
    
# saludo_personalizado()
print("hasta pronto .....")

'''
Script en Pethon que dentro de un procedimiento solicite el nombre y la edad del usuario y en caso de ser mayor o igual a 18 le indique que es mayor de edad, en caso contrario indicarle que es menor.
'''

def mayoria_edad():
    nombre = input("¿ Cual es tu nombre? ")
    edad = int(input("¿Que edad tienes? "))
    if edad >= 18:
        print(f"Hola {nombre} Eres mayor de Edad")
    else:
        print(f"Hola {nombre} Eres menor de edad")
mayoria_edad()
print(" Hasta luego ......")