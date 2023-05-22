usuarios = [
    ["yo", 12],
    ["ello", 2],
    ["superyo", 90]
]
# así se accede al primer elemento de la lista
# nombres = [usuario[0] for usuario in usuarios]

#filtrar
# nombres = [usuario for usuario in usuarios if usuario[1] > 2]

# mapear
# nombres = list(map(lambda usuario:usuario[0], usuarios))

# filtrar
menosUsuarios = list(filter(lambda usuario: usuario[1]>2, usuarios))
print(menosUsuarios)