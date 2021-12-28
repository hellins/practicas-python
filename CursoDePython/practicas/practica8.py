'''
Anidamiento estructural
script en Python que simula un juego de preguntas y respuestas, si el usuario contesta correctamente una pregunta puede continuar con ña siguiente, en caso de fallar se le indica que ha perdido.
Si contesta todas las preguntas se le felicita por du conocimiento.
'''
print("Bienvenid@ pongamos a prueba tus conocimioentos: V")
respuesta = int(input("¿Cual seria de la velocidad de la luz m/s ? "))
if respuesta == 299792458:
    print("¡Correcto")
    respuesta = int(input("¿Cuanto es 8+8/8*8? "))
    if respuesta == 8+8/8*8:
        print("¡Correcto")
        respuesta = input("¿De que color eran las mangas del chaleco de napoleon  ?")
        if respuesta == "Los chalecos no tienen mangas":
            print("¡Correcto")
            print("Felicitaciones respondistes todas las preguntas correctamente")
        else:
            print("Respuesta incorrecta")
    else:
        print("Lo siento respuesta incorrecta")
else:
    print("Lo siento respuesta incorrecta")
print("Hasta luego")