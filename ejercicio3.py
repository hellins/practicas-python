palabra1 = input("Ingresa la primera palabra: ")
palabra2 = input("Ingresa la Segunda palabra: ")

if len(palabra1) < 3 or len(palabra2) < 3:
    print("No riman, porque tienen monos de 3 caracteres")
elif palabra1[-3 :] ==  palabra2[-3 : ]:
    print("Las palabras riman")
elif palabra1[-2 : ] == palabra2[-2 : ]:    
    print("Las palabras riman poco")
else:
    print(" las palabras no riman")    