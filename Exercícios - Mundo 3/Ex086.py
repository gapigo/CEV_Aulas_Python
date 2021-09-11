matriz = list()
linha = list()

for i in range(0, 3):
    for j in range(0, 3):
        linha.append(int(input(f'Digite o elemento ({i},{j}) = ')))
    matriz.append(linha[:])
    linha.clear()
print('=~' * 15)
for i in range(0, 3):
    print(f'      [{matriz[i][0]:^5}]  [{matriz[i][1]:^5}]  [{matriz[i][2]:^5}]      ')
print('=~' * 15)
