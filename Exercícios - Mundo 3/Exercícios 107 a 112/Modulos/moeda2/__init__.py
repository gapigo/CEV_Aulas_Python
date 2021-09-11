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
