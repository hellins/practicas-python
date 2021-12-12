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
    