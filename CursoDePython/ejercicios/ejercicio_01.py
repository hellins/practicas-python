'''
Estructura Repetitiva
script en Python que implemente el juego de adivinar un numero, pero esta vez en modo competitivo. La computadora debera generar un numero aleatorio en 1 y 100 y tanto el usuario como la computadora deberan intentar adivinar dicho numerio. Para que el juego sea retador el jugador maquina debera ser "inteligente" y competir para ganar. El juego se realizara por turnos, primero la maquina y despues el usuario y por cada intento la computadora respondera si el numero es mayor o menor que el secretro.
'''

import os
import random

secreto = random.