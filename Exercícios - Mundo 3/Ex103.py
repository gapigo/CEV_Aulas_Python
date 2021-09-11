def ficha(nome='<desconhecido>', gols=0):
    print(f'O jogador {nome} fez {gols} gol(s) no campeonato.')


print('-' * 40)
nome = str(input('Nome do jogador: ')).title()
gols = str(input('Número de gols: ')).title()

if gols.isnumeric() and (nome.upper() or nome.lower()):
    ficha(nome, gols)
elif gols.isnumeric():
    ficha(gols=int(gols))
else:
    ficha()