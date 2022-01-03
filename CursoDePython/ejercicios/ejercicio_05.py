''''
Estructura Repetitiva
script en Python que muestre un cronometro en formato de 24 horas. El despligue seguira el formato h:m:s. El cronograma debera iniciar en 0:0:0 y podra legar hasta 23:59:59. Implementar retardo de 1 segundo y limpieza de pantalla de forma tal que solo se vea  un tiempo en pantalla.
'''
import time
import os

for hora in range(24):
    for minuto in range (60):
        for segundo in range(60):
            os.system("clear")
            print(f"{hora}:{minuto}:{segundo}")
            time.sleep(1)
            
