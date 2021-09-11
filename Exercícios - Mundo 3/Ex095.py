from time import sleep

jogador = dict()
jogadores = list()
partidas = list()
aux = list()

while True:
    jogador['Nome'] = str(input('Digite seu nome: ')).strip().title()
    jogador['Total de partidas'] = int(input('Digite seu total de partidas: '))
    soma = 0
    for c in range(0, jogador['Total de partidas']):
        partidas.append(int(input(f'Digite a quantidade de gols na partida {c}: ')))
        soma += partidas[c]
    jogador['Total de gols'] = soma
    jogador['Partidas'] = partidas[:]
    partidas.clear()
    jogadores.append(jogador.copy())
    jogador.clear()
    opc = str(input('Deseja continuar? [S/N] ')).strip().lower()[0]
    if opc in 'n':
        break

while True:
    print('=~' * 16)
    print(f'{"No.":<3}{"JOGADOR":<15}{"TOTAL":^7}{"GOLS"}')
    i = 0
    for jogador in jogadores:
        print(f'{i:<3}{jogador["Nome"]:<15}{jogador["Total de gols"]:^7}{jogador["Partidas"]}')
        i += 1
    print('=~' * 16)
    opc = int(input('Escolha o número de um jogador para ver os gols por partida: (-1 pra sair) '))
    if opc == -1:
        break
    elif opc < len(jogadores):
        print('=~' * 16)
        print(f'O jogador {jogadores[opc]["Nome"]} fez:')
        for pos, gols in enumerate(jogadores[opc]["Partidas"]):
            print(f'{gols} gols na partida {pos}')
            sleep(1)
        print(f'Totalizando {jogador["Total de gols"]} durante o campeonato')
        sleep(2)
    else:
        print(' >> OPÇÃO INVÁLIDA, TECLE NOVAMENTE! <<')
print(' >> VOLTE SEMPRE <<')
