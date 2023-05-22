lista = [1,2,3,4]
lista2 = [5,6,7,8]
print(*lista, *lista2) #agregar un asterico desempaqueta la lista

punto1 = {"x":10}
punto2 = {"y":25}
nuevo = {**punto1, **punto2} #agregar dos asteriscos desempaqueta diccionarios
print(nuevo)