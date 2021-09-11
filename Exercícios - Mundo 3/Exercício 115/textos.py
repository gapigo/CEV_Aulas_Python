def linhas(num=40, semPular = False):
    if not semPular:
        print('-' * num)
    else:
        print('-' * num, end='')


def título(mensagem, tamanho=40):
    linhas(tamanho)
    print(f'{mensagem:^{tamanho}}')
    linhas(tamanho)


def opcCol(nomeOpcao, color):
    from cores import cor
    cor(f'{nomeOpcao}', color, pularLinha=False)
    print(' - ',end='')


def selInt(inicio, fim, mensagem):
    """
    seleciona números inteiros válidos
    :param inicio: número inicial
    :param fim: número final
    :param mensagem: mensagem de input
    :return: inteiro
    """
    from dados import lerInt
    from cores import cor
    while True:
        num = lerInt(mensagem)
        if num < inicio or num > fim:
            cor('Opção fora do escopo!', 'vermelho', pularLinha=True)
        else:
            return num
