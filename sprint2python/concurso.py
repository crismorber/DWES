import random
print("¡Adivina la respuesta correcta!")

puntuacion=0
veces=0
repeticion1=0
repeticion2=0
repeticion3=0
preguntas = ["¿En qué año tuvo lugar la pandemia del coronavirus?","¿Cuántos colores tiene el arcoiris?","¿Qué idioma se habla en Moldavia?"]


while veces < 3 :
    numeroRandom=random.randint(1,3)
    if numeroRandom==1 and repeticion1<2:
        repeticion1+=1
        veces+=1
        print(preguntas[0])
        respuesta=None

        print("a) 2022")
        print("b) 2019")
        print("c) 2020")
        respuesta = input ("Introduce una de las opciones (a, b, c): ")
        while (respuesta !="a" and respuesta !="b" and respuesta!="c"):
            respuesta = input ("Introduce una de las opciones (a, b, c): ")
        if (respuesta=="b" or respuesta =="a"):
            print("Respuesta incorrecta :( Pierdes 5 puntos")
            puntuacion = puntuacion - 5
        elif (respuesta == "c"):
            print("Respuesta correcta :) Ganas 10 puntos")
            puntuacion = puntuacion + 10

    if numeroRandom==2 and repeticion2<2:  
        repeticion2+=1
        veces+=1     
        print(preguntas[1])
        respuesta=None
        print("a) 7")
        print("b) 9")
        print("c) 8")
        respuesta = input ("Introduce una de las opciones (a, b, c): ")
        while (respuesta !="a" and respuesta !="b" and respuesta!="c"):
            respuesta = input ("Introduce una de las opciones (a, b, c): ")
        if (respuesta=="c" or respuesta =="b"):
            print("Respuesta incorrecta :( Pierdes 5 puntos")
            puntuacion = puntuacion - 5
        elif (respuesta == "a"):
            print("Respuesta correcta :) Ganas 10 puntos")
            puntuacion = puntuacion + 10

    if numeroRandom==3 and repeticion3<2: 
        repeticion3+=1
        veces+=1      
        print(preguntas[2])
        respuesta=None

        print("a) Ruso")
        print("b) Rumano")
        print("c) Inglés")
        respuesta = input ("Introduce una de las opciones (a, b, c): ")
        while (respuesta !="a" and respuesta !="b" and respuesta!="c"):
            respuesta = input ("Introduce una de las opciones (a, b, c): ")
        if (respuesta=="a" or respuesta =="c"):
            print("Respuesta incorrecta :( Pierdes 5 puntos")
            puntuacion = puntuacion - 5
        elif (respuesta == "b"):
            print("Respuesta correcta :) Ganas 10 puntos")
            puntuacion = puntuacion + 10


print("Gracias por jugar <3 tu puntuación es de ", puntuacion, " puntos" )
if puntuacion==30:
    print("Felicidades, las acertaste todas!")