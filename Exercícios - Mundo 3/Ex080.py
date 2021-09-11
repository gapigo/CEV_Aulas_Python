lista = list()
pos = cont = aux = 0

while True:
    num = int(input('Digite um número: '))
    pos = 0
    if cont == 0 or num > lista[-1]:
        lista.append(num)
    else:
        for pos, atual in enumerate(lista):
            if atual > num:
                break
        lista.insert(pos, num)
    print(f'Lista: {lista}')
    opcao = str(input('Deseja continuar? [S/N]')).strip().lower()[0]
    if opcao in 'n':
        break
    cont += 1
print(f'A lista ordenada dos {len(lista)} por você digitados é {lista}')
