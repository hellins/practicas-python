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
print("Se medira la temperatura")

temp = int(input("introduzca el valor de la temperatura: "))

if 18<= temp <=27:
    print("La temperatura es agradable")
print("Nos vemos pronto")    