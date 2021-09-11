def dobro(num, formatar=False):
    resp = num*2
    if not formatar:
        return resp
    else:
        return f'R${resp:.2f}'


def metade(num, formatar=False):
    resp = num/2
    if not formatar:
        return resp
    else:
        return f'R${resp:.2f}'


def aumentar(num, porcentagem, formatar=False):
    resp = num + (num/100*porcentagem)
    if not formatar:
        return resp
    else:
        return f'R${resp:.2f}'


def diminuir(num, porcentagem, formatar=False):
    resp = num - (num / 100 * porcentagem)
    if not formatar:
        return resp
    else:
        return f'R${resp:.2f}'


def moeda(num):
    return f'R${num:.2f}'


def resumo(preço, paumentar, pdiminuir):
    print('-='*15)
    print('{:^30}' .format('RESUMO DO VALOR'))
    print('-='*15)
    print(f'Preço analisado:    R${preço:.2f}')
    print(f'Dobro do preço:     R${dobro(preço):.2f}')
    print(f'Metade do preço:    R${metade(preço):.2f}')
    print(f'{paumentar}% de aumento:     R${aumentar(preço, paumentar):.2f}')
    print(f'{pdiminuir}% de redução:     R${diminuir(preço, pdiminuir):.2f} ')
    print('-=' * 15)
