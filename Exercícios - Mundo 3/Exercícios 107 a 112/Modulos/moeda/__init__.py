def dobro(num):
    return num*2


def metade(num):
    return num/2


def aumentar(num, porcentagem):
    return num + (num/100*porcentagem)


def diminuir(num, porcentagem):
    return num - (num / 100 * porcentagem)


def moeda(num):
    return f'R${num:.2f}'


def resumo(preço, paumentar, pdiminuir):
    print('-='*15)
    print('{:^30}' .format('RESUMO DO VALOR'))
    print('-='*15)
    print(f'Preço analisado:    R${preço}')
    print(f'Dobro do preço:     R${dobro(preço)}')
    print(f'Metade do preço:    R${metade(preço)}')
    print(f'{paumentar}% de aumento:     R${aumentar(preço, paumentar)}')
    print(f'{pdiminuir}% de redução:     R${diminuir(preço, pdiminuir)} ')
    print('-=' * 15)
