from factorial import func_factorial
from factorial2 import func_factorial2

numero=input("Introduce un número para calcular su factorial recursivamente:")

resultado = func_factorial(int(numero))

print (resultado)

numero2=input("Introduce un número para calcular su factorial no recursivamente:")

resultado2 = func_factorial2(int(numero2))

print (resultado2)
