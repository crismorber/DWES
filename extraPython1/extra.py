import random
from select import select

print ("¡Bienvenido a Piedra, Papel o Tijera!")

puntuacion = 0
contadorRepeticiones=0

jugadasMaquina = ["Piedra","Papel","Tijera"]



while contadorRepeticiones<5:
    jugadaMaquina= random.choice(jugadasMaquina)
    respuesta = input ("Introduce tu jugada: Piedra, Papel o Tijera: ")
    while (respuesta!= "Piedra" and respuesta!="Papel" and respuesta!="Tijera"):
       respuesta = input ("Introduce tu jugada: Piedra, Papel o Tijera: ")

    if respuesta=="Piedra":
        print("La máquina escogió ",jugadaMaquina)
        if jugadaMaquina=="Tijera":
            puntuacion+=1
            contadorRepeticiones+=1
            print ("Ganaste esta ronda!, llevas: ",puntuacion, " rondas ganadas")
        elif jugadaMaquina=="Papel":
            contadorRepeticiones+=1
            print ("Perdiste esta ronda. Llevas: ",puntuacion, " rondas ganadas")
        else:
            print ("Quedásteis empate, esta ronda no cuenta.")
    if respuesta=="Tijera":
        print("La máquina escogió ",jugadaMaquina)
        if jugadaMaquina=="Papel":
            puntuacion+=1
            contadorRepeticiones+=1
            print ("Ganaste esta ronda!, llevas: ",puntuacion, " rondas ganadas")
        elif jugadaMaquina=="Piedra":
            contadorRepeticiones+=1
            print ("Perdiste esta ronda. Llevas: ",puntuacion, " rondas ganadas")
        else:
            print ("Quedásteis empate, esta ronda no cuenta.")
    if respuesta=="Papel":
        print("La máquina escogió ",jugadaMaquina)
        if jugadaMaquina=="Piedra":
            puntuacion+=1
            contadorRepeticiones+=1
            print ("Ganaste esta ronda!, llevas: ",puntuacion, " rondas ganadas")
        elif jugadaMaquina=="Tijera":
            contadorRepeticiones+=1
            print ("Perdiste esta ronda. Llevas: ",puntuacion, " rondas ganadas")
        else:
            print ("Quedásteis empate, esta ronda no cuenta.")
if puntuacion>=3:
    print("Felicidades ganaste <3")
else:
    print("Perdiste. Suerte la proxima vez.")
