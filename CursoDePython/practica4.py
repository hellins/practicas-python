'''
selectiva simple
script en python solicitar calificaion y asisyencia al curso
Si la calificacion es mayor o igul a 60 y la asistencia es mayor a 20 el alumno aprueba
'''
'''

calificacion = int(input("Cual es tu calicicacion: "))
asistencia = int(input(" cuantas veces asistio a clases: "))

if calificacion >= 60 and asistencia >= 20:
    print("Felicitaciones Aprobastes el Curso de Python")
    if calificacion >= 95:
        print("Felicitaciones eres sobresaliente tienes una beca")
    
print("Sigue disfrutando tu Dia") 
'''
'''
Script de python que pregunte al usuario cuanto es la temperatura del termometroy si ese valor
se encuentra entre 18 y 27 que indique la temperatura es agradable
'''
'''print("Se medira la temperatura")

temp = int(input("introduzca el valor de la temperatura: "))

if 18<= temp <=27:
    print("La temperatura es agradable")
print("Nos vemos pronto")  
print("hola")  
'''
# Sistema de redondeo de notas
# El usuario debe cargar la calificacion, si la calificacion le falta 0,4 o menos para
# el siguiente multiplo de 10 , entonces su calificacion sera redondeada al siguiente 
# multiplo de 10, en caso contrario su calificacion no sera modidicada.

import math

nota = float(input("Ingresa tu Calificacion: "))

calificacion = round(nota)

print(f"Tu calificacion es: {calificacion}")
if calificacion >= 10:
    print("Bien hecho aprobaste la materia !!!")
    if calificacion >= 16:
        print("Excelente eximiste la Materia")
        
print("Sigue estudiando")
        
'''
numero = 1.5
redondeado = round(numero)
redondeado_abajo = math.floor(numero)
redondeado_arriba = math.ceil(numero)
print("Redondeado con round: {}".format(redondeado))
print("Redondeado con floor (hacia abajo): {}".format(redondeado_abajo))
print("Redondeado con ceil (hacia arriba): {}".format(redondeado_arriba))
'''

nota1 = int(input(" Ingresa otra calificacion: "))
redondeo = nota1 % 10

if 0 <= nota1 <= 100 and redondeo >=6:
    nota1 = nota1 + (10 - redondeo)
    
print(nota1)
 