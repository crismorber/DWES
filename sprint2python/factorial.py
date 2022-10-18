def func_factorial(numero: int):
  
    if (numero==1 or numero==0):
        return 1
    elif numero > 1:
        return numero * func_factorial(numero - 1)