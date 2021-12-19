'''
Selectiva multiple
Script en Python que muestre un menu con los nombre de distintos paises de America y si el ususrio selecciona alguna de las opciones se le mostrara el nomnre e la caítal de ese pais.
'''

MEXICO = 1
URUGUAY = 2
COLOMBIA = 3
ARGENTINA =4
ECUADOR = 5
PERU = 6
VENEZUELA = 7

print('''                                   Capitales de America
1) Mexico
2) Uriguay
3) Colombia
4) Argentina
5) Ecuador
6) Peru
7) Venezuela
''')
opc = int(input("Selecciona una opcion: "))

if opc == MEXICO:
    print("Ciudad de Mexico")
elif opc == URUGUAY:
    print("Montevideo")
elif opc == COLOMBIA:
    print("Bogota")
elif opc == ARGENTINA:
    print("Buenos Aires")
elif opc == ECUADOR:
    print("Quito")
elif opc == PERU:
    print("Lima")
elif opc == VENEZUELA:
    print("Caracas")
else:
    print("Opcion no valida")
print("Que tengas un buen dia")
