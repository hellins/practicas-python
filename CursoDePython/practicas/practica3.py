'''
Selectiva simple
script en paython 

edad = int(input("hola cuantos años tienes: "))
if edad >= 18:
    print("Eres Mayor de Edad")
else:
    print("Eres Menor de Edad")
print("Que tengas un excelente dia")   
'''
import random

secreto = random.randint(1, 10)

print("he generado un numero aleatorio del 1 al 10. Intenta adivonarlo")
numero = int(input("Cual cres que sea el numero? "))

if numero == secreto:
    print(f"Lograste Aserta el numero: {secreto}")
    
print("Sigue disfrutando tu dia")

# Selectiva Dobole
# Script de Python que solocite al usuario que intente adivinar un numero del 1 al 10.
# Si lo ado
# adivina lo felicita por su logro, en caso contrario le indica cual era el numero secreto

# import random

secreto1 = random.randint(1, 10)

print("he generado un numero aleatorio del 1 al 10. Intenta adivonarlo")
usuario = int(input("Cual crees que seri el numero secreto: "))

if usuario == secreto1:
    print("Lograste adivinar el numero")
else:
    print(f"No lograste adivinar, el numero secreto es: {secreto1}")
    
print("Gracias por participar !!!")        
    