def func_factorial2(numero: int):
    if numero ==0:
        return 1

    factorial=1
    while numero > 0:
        factorial = factorial * numero 
        numero -= 1


    return factorial
