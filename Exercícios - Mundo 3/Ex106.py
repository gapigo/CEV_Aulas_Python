def trata(mensagem):
    return mensagem.strip().lower()


def título(mensagem):
    print('~' * (len(mensagem) + 4))
    print(f'  {mensagem}')
    print('~' * (len(mensagem) + 4))


def cor(color, mensagem, titulo=False):
    if color.strip().lower() in 'branco':
        print('\033[7;30;m', end='')
    elif color.strip().lower() in 'vermelhovermelha':
        print('\033[0;30;41m', end='')
    elif color.strip().lower() in 'verde':
        print('\033[0;30;42m', end='')
    elif color.strip().lower() in 'amarelo':
        print('\033[0;30;43m', end='')
    elif color.strip().lower() in 'azul':
        print('\033[0;30;44m', end='')
    elif color.strip().lower() in 'roxoliláslilas':
        print('\033[0;30;45m', end='')
    elif color.strip().lower() in 'ciano':
        print('\033[0;30;46m', end='')
    elif color.strip().lower() in 'padrãocinza':
        print('\033[0;30;47m', end='')
    if titulo:
        título(mensagem)
    else:
        print(mensagem)
    print('\033[m', end='')


def ajuda(mensagem):
    print('\033[7;30m')
    help(mensagem)
    print('\033[m', end='')

# Programa Principal

while True:
    cor('verde', 'SISTEMA DE AJUDA PyHELP', titulo=True)
    opção = trata(input('Função ou Biblioteca > '))

    if opção == 'fim':
        break
    else:
        cor('azul', f'Acessando o manual do comando {opção}', titulo=True)
        ajuda(opção)
cor('vermelho', 'ATÉ LOGO!', titulo=True)
