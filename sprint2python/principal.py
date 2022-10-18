from factorial import func_factorial
from factorial2 import func_factorial2
import time

print ("a) Factorial de un número recursivamente")
print ("b) Factorial de un número no recursivamente")
respuesta = input("Elige una de las dos opciones (a o b): ")

while (respuesta!="a" and respuesta!="b"):
    respuesta = input("Elige una de las dos opciones (a o b): ")

if respuesta == "a":
    tiempo_inicio=time.time()
    numero=input("Introduce un número para calcular su factorial recursivamente: ")
    resultado = func_factorial(int(numero))
    print ("El factorial de",numero, "es", resultado)
    tiempo_fin=time.time()
    tiempo_transcurrido=tiempo_fin-tiempo_inicio
    print("El tiempo de ejecución ha sido : ", str(tiempo_transcurrido) + 's')
elif respuesta == "b":
    tiempo_inicio=time.time()
    numero=input("Introduce un número para calcular su factorial no recursivamente: ")
    resultado = func_factorial(int(numero))
    print ("El factorial de",numero, "es", resultado)
    tiempo_fin=time.time()
    tiempo_transcurrido=tiempo_fin-tiempo_inicio
    print("El tiempo de ejecución ha sido : ", str(tiempo_transcurrido) + 's')

    
