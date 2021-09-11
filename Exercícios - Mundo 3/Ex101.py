def voto(ano):
    from datetime import date
    atual = date.today().year
    idade = atual - ano
    if idade < 16:
        return f'NEGADO'
    elif idade < 18 or idade >= 65:
        return 'OPCIONAL'
    else:
        return 'OBRIGATÓRIO'


opção = voto(int(input('Digite o ano de seu nascimento: ')))
print(f'Em eleição, você tem voto {opção}')
