cores = {'vermelho': '\033[31m',
         'verde'   : '\033[32m',
         'amarelo' : '\033[33m',
         'azul'    : '\033[34m',
         'roxo'    : '\033[35m',
         'ciano'   : '\033[36m',
         'cinza'   : '\033[37m',
         'default' : '\033[::m'}


def cor(mensagem, opcao, pularLinha=False, pintarTudo=False, imprimir=True):
    opcao = opcao.strip().lower().replace(' ', '')
    if imprimir:
        if opcao in 'vermelhovermelhared':
            print(f'{cores["vermelho"]}{mensagem}', end='')
        elif opcao in 'verdegreen':
            print(f'{cores["verde"]}{mensagem}', end='')
        elif opcao in 'amareloamarelayellow':
            print(f'{cores["amarelo"]}{mensagem}', end='')
        elif opcao in 'azulblue':
            print(f'{cores["azul"]}{mensagem}', end='')
        elif opcao in 'roxoliláslilaspurple':
            print(f'{cores["roxo"]}{mensagem}', end='')
        elif opcao in 'cianocyan':
            print(f'{cores["ciano"]}{mensagem}', end='')
        elif opcao in 'cinzagrey':
            print(f'{cores["cinza"]}{mensagem}', end='')
        if pularLinha:
            print()
        if not pintarTudo:
            print(f'{cores["default"]}', end='')
    else:
        string = ''
        if opcao in 'vermelhovermelhared':
            string = f'{cores["vermelho"]}{mensagem}'
        elif opcao in 'verdegreen':
            string = f'{cores["verde"]}{mensagem}'
        elif opcao in 'amareloamarelayellow':
            string = f'{cores["amarelo"]}{mensagem}'
        elif opcao in 'azulblue':
            string = f'{cores["azul"]}{mensagem}'
        elif opcao in 'roxoliláslilaspurple':
            string = f'{cores["roxo"]}{mensagem}'
        elif opcao in 'cianocyan':
            string = f'{cores["ciano"]}{mensagem}'
        elif opcao in 'cinzagrey':
            string = f'{cores["cinza"]}{mensagem}'
        if pularLinha:
            string += '\n'
        if not pintarTudo:
            string += f'{cores["default"]}'
        return string
