jogador = dict()
jogador['Nome'] = str(input('Digite seu nome: ')).strip().title()
jogador['Total de partidas'] = int(input('Digite seu total de partidas: '))
soma = 0
for c in range(0, jogador['Total de partidas']):
    jogador[f'Partida {c}'] = int(input(f'Digite a quantidade de gols na partida {c}: '))
    soma += jogador[f'Partida {c}']
jogador['Total de gols'] = soma
print(f'O jogador {jogador["Nome"]} fez em {jogador["Total de partidas"]} partidas:')
for c in range(0, jogador['Total de partidas']):
    print(f'{jogador[f"Partida {c}"]} gols na partida {c}')
print(f'Totalizando {jogador["Total de gols"]} durante o campeonato')
