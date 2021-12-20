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

print('''                                   CALCULADORA
1) Suma
2) Resta
3) Multiplicacion
4) Division
5) Division Entera
6) Modulo
7) Potencia
      ''')

SUMA = 1
RESTA = 2
MULTI = 3
DIVI = 4
DIVI_ENTE = 5
MODULO = 6
POTENCIA = 7

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