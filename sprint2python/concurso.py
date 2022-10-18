print("¡Adivina la respuesta correcta!")

puntuacion=0

preguntas = ["¿En qué año tuvo lugar la pandemia del coronavirus?","¿Cuántos colores tiene el arcoiris?","¿Qué idioma se habla en Moldavia?"]

for i in range(3): 
    print(preguntas[i])
    respuesta=None

    if i==0:
        print("a) 2022")
        print("b) 2019")
        print("c) 2020")
        respuesta = respuesta = input ("Introduce una de las opciones (a, b, c): ")
        while (respuesta !="a" and respuesta !="b" and respuesta!="c"):
            respuesta = respuesta = input ("Introduce una de las opciones (a, b, c): ")
        if (respuesta=="b" or respuesta =="a"):
            print("Respuesta incorrecta :( Pierdes 5 puntos")
            puntuacion = puntuacion - 5
        elif (respuesta == "c"):
            print("Respuesta correcta :) Ganas 10 puntos")
            puntuacion = puntuacion + 10
    if i==1:
        print("a) 7")
        print("b) 9")
        print("c) 8")
        respuesta = respuesta = input ("Introduce una de las opciones (a, b, c): ")
        while (respuesta !="a" and respuesta !="b" and respuesta!="c"):
            respuesta = respuesta = input ("Introduce una de las opciones (a, b, c): ")
        if (respuesta=="c" or respuesta =="b"):
            print("Respuesta incorrecta :( Pierdes 5 puntos")
            puntuacion = puntuacion - 5
        elif (respuesta == "a"):
            print("Respuesta correcta :) Ganas 10 puntos")
            puntuacion = puntuacion + 10
    if i==2:
        print("a) Ruso")
        print("b) Rumano")
        print("c) Inglés")
        respuesta = respuesta = input ("Introduce una de las opciones (a, b, c): ")
        while (respuesta !="a" and respuesta !="b" and respuesta!="c"):
            respuesta = respuesta = input ("Introduce una de las opciones (a, b, c): ")
        if (respuesta=="a" or respuesta =="c"):
            print("Respuesta incorrecta :( Pierdes 5 puntos")
            puntuacion = puntuacion - 5
        elif (respuesta == "b"):
            print("Respuesta correcta :) Ganas 10 puntos")
            puntuacion = puntuacion + 10


print("Gracias por jugar <3 tu puntuación es de ", puntuacion, " puntos" )
if puntuacion==30:
    print("Felicidades, las acertaste todas!")