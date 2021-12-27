'''
Selectiva Multuiple
Script en Python que simule una calculadora con la operaciones arismeticas basicas. El menu mostrado sera el siguiente:

1) Suma
2) Resta
3) Multiplicacion
4) Division
5) Division Entera
6) Modulo
7) Potencia
'''

SUMA = 1
RESTA = 2
MULTIPLICACION = 3
DIVISION = 4
DIVISION_ENTERA = 5
MODULO = 6
POTENCIA = 7

print(f'''                                   CALCULADORA
{SUMA}) Suma
{RESTA}) Resta
{MULTIPLICACION}) Multiplicacion
{DIVISION}) Division
{DIVISION_ENTERA}) Division Entera
{MODULO}) Modulo
{POTENCIA}) Potencia
''')

opc = int(input("Selecciona una opcion: "))
if SUMA <= opc <= POTENCIA:
    op_1 = int(input("Primer operando: "))
    op_2 = int(input("Segundo operando: "))
    if opc == SUMA:
        print(f"La Suma de {op_1} + {op_2} = {op_1+op_2}")
    elif opc == RESTA:
        print(f"La Resta de {op_1} - {op_2} = {op_1-op_2}")
    elif opc == MULTIPLICACION:
        print(f"La Multiplicacion de {op_1} x {op_2} = {op_1*op_2}")
    elif opc == DIVISION:
        print(f"La Division de {op_1} / {op_2} = {op_1/op_2}")
    elif opc == DIVISION_ENTERA:
        print(f"La Division Entera de {op_1} // {op_2} = {op_1//op_2}")
    elif opc == MODULO:
        print(f"El Modulo de {op_1} % {op_2} = {op_1%op_2}")
    elif opc== POTENCIA:
        print(f"La Potencia de {op_1} ** {op_2} = {op_1**op_2}")
else:
    print("Opcion no valida") 

'''

opc = int(input("Seleccione Operacion Arismetica: "))
if SUMA <= opc <= POTENCIA:
    if opc == SUMA:
        suma1 = int(input("Ingresa primer numero a sumar: "))
        suma2 = int(input("Ingresa segundo numero a sumar: "))
        resuma = suma1 + suma2
        print(f"El resultado de la suma de {suma1} + {suma2} es: {resuma}")
    elif opc == RESTA:
        resta1 = int(input("ingresa primer numero a restar: "))
        resta2 = int(input("Ingresa segundo numero a restar: "))
        resuresta = resta1 - resta2
        print(f"El resultado de la resta de {resta1} - {resta2} es: {resuresta}")
    elif opc == MULTI:
        multi1 = int(input("Ingresa primer numero a Multiplicar: "))
        multi2 = int(input("Ingresa segundo numero a Multiplicar: "))        
        resumulti = multi1 * multi2
        print(f"El Resultado de la Multiplicaion de {multi1} x {multi2} es: {resumulti}")
    elif opc == DIVI:
        divi1 = int(input("ingresa el dividendo: "))
        divi2 = int(input(" ingrese el divisor: "))
        if divi2 == 0:
            print("No se puede dividir entre cero (0)")
        else:
            resudivi = divi1 / divi2
            print(f"El resultado de la Division de {divi1} / {divi2} es: {resudivi}")
    elif opc == DIVI_ENTE:
        divi_ente1 = int(input("Ingresa el dividendo:"))
        divi_ente2 = int(input(" ingrese el divisor: "))
        if divi_ente2 == 0:
            print("No se puede dividir entre cero (0)")
        else:
            resudivi_ente = int
            resudivi_ente = divi_ente1 // divi_ente2
            print(f"El resultado de la Division de {divi_ente1} / {divi_ente2} es: {resudivi_ente}")

else:
    print("Opcion no valida")
'''