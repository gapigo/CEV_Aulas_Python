lista = list()
pares = list()
ímpares = list()

while True:
    lista.append(int(input('Digite um número: ')))
    opcao = str(input('Deseja continuar? [S/N] ')).strip().lower()[0]
    if opcao in 'n':
        break
for atual in lista:
    if atual % 2 == 0:
        pares.append(atual)
    else:
        ímpares.append(atual)
print(f'Os números pares foram: {pares}')
print(f'E os ímpares foram: {ímpares}')
