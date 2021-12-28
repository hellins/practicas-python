'''
Estructura Repetitiva
script en Python que implemente el juego de adivinar un numero, pero esta vez en modo competitivo. La computadora debera generar un numero aleatorio en 1 y 100 y tanto el usuario como la computadora deberan intentar adivinar dicho numerio. Para que el juego sea retador el jugador maquina debera ser "inteligente" y competir para ganar. El juego se realizara por turnos, primero la maquina y despues el usuario y por cada intento la computadora respondera si el numero es mayor o menor que el secretro.
'''

import os
import random

inferior = 1
superoir = 100
secreto = random.randint(1, 100)
usuario = -1
maquina = -1

while usuario != secreto and maquina != secreto:
    os.system("clear")
    print("Maquina ¿Cual crees que sea el numero sercreto? ")
    maquina = random.randint(inferior, superoir)
    print(f"Maquina: {maquina}")
    if maquina < secreto:
        print("Tu numero es menor")
        inferior = maquina + 1
    elif maquina > secreto:
        print("Tu numero es mayor")
        superoir = maquina - 1
    else:
        print("Ha ganado la Maquina ....")
    if maquina != secreto:
        usuario = int(input("Usuario, ¿Cual crees que sea el número secreto: ?"))
        if usuario < secreto:
            print("tu numero es menor")
            if usuario > inferior:
                inferior = usuario +1
        elif usuario > secreto:
            print("Tu numero es mayor")
            if usuario < superoir:
                superoir = usuario - 1
        else:
            print("El usuario  ha  ganado")
    input("presina enter para continuar.....")
input("Nos vemos.....")