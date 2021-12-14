'''
Selectiva doble
script en Python que simule el sistema de validacion de una platafrma digital. El usuaio 
debera proporcionar tanto su nombre como la contraseña. Si los valores cinciden con los
previamenta almacenados entonces se le dara la bienvenida, si no le indicara que hubo 
un error.
'''

USER = "pepe"
PASSWORD = "pepe123"

print("Proporciona los datos siguientes: ")

user = input("Usuario: ")
password = input("Contraseña: ")

if user == USER and password == PASSWORD:
    print("Bienvenido a tu cuenta")
else:
    print(" Datos incorrectos ")
    
# Estructura Selectiva Multiple
'''
Script en Python que solicite al usuario una calificacion y una cantidad de asistencias a un
curso. Si la calificacion y la cantidad de asistencias son aprobatorias en tonces se le 
felicita por su logro; en caso contrario sele indicara en que fallo. La cailificacion
minima aprobatoria sera  de 60 y la cantidad minima de asiatencia sera de 24.
'''

