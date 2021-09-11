matriz = list()
linha = list()
sPares = s3c = m2l = 0

for i in range(0, 3):
    for j in range(0, 3):
        linha.append(int(input(f'Digite o elemento ({i},{j}) = ')))
    matriz.append(linha[:])
    linha.clear()
print('=~' * 15)
for i in range(0, 3):
    print(f'      [{matriz[i][0]}:^3]  [{matriz[i][1]}:^3]  [{matriz[i][2]}:^3]      ')
print('=~' * 15)
for linha in matriz:
    for num in linha:
        if num % 2 == 0:
            sPares += num
print(f'A soma dos valores pares é {sPares}')

for i in range(0, 3):
    s3c += matriz[i][2]

print(f'A soma dos valores da terceira coluna é {s3c}')

for i in range(0, 3):
    if i == 0:
        m2l = matriz[1][0]
    elif m2l < matriz[1][i]:
        m2l = matriz[1][i]

print(f'E o maior da segunda linha é {m2l}')
