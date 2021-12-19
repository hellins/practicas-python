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
curso. Si la calificacion y la cantidad de asistencias son aprobatorias entonces se le 
felicita por su logro; en caso contrario sele indicara en que fallo. La cailificacion
minima aprobatoria sera  de 60 y la cantidad minima de asiatencia sera de 24.
'''

MIN_CAL = 60
MIN_ASI = 24

print("Por favon inrgresa los siguientes datos: ")
cal = int(input("Colocca tu calificacion: "))
asi = int(input("Ingrrsa tu Asistencia: "))
          
if cal >= MIN_CAL and asi >= MIN_ASI:
    print("Aprobaste la Materia Felicitaciones")
elif cal < MIN_CAL and asi >= MIN_ASI:
    print(f"Calificacion insuficiente. El minimo es: {MIN_CAL}")
elif cal >= MIN_CAL and asi < MIN_ASI:
    print(f"Asisstencias insuficientes. La minima es: {MIN_ASI}")
else:
    print(f"Calificacion y Asistencias insuficiente. La Calificacion mininima es: {MIN_CAL} y la asistencia minima es {MIN_ASI}")
print("Que tengas un buen dia")  