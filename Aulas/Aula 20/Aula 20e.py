def dobra(list):
    i = 0
    while i < len(list):
        list[i] *= 2
        i += 1


# Começo do programa
lista = [5, 9, 7, 6, 5]
print(lista)
dobra(lista)
print(lista)
