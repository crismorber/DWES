from factorial import func_factorial
from factorial2 import func_factorial2

print ("a) Factorial de un número recursivamente")
print ("b) Factorial de un número no recursivamente")
respuesta = input("Elige una de las dos opciones (a o b): ")

while (respuesta!="a" and respuesta!="b"):
    respuesta = input("Elige una de las dos opciones (a o b): ")

if respuesta == "a":
    numero=input("Introduce un número para calcular su factorial recursivamente: ")
    resultado = func_factorial(int(numero))
    print ("El factorial de",numero, "es", resultado)
elif respuesta == "b":
    numero=input("Introduce un número para calcular su factorial no recursivamente: ")
    resultado = func_factorial2(int(numero))
    print ("El factorial de",numero, "es", resultado)

    
