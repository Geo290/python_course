def suma(*numeros): #así se admiten varios parametros
    resultado = 0
    for numero in numeros:
        resultado += numero
    print(resultado)

suma(2,3,20)