from random import randint
from time import sleep
from operator import itemgetter

jogadas = dict()
ranking = dict()

for i in range(1, 5):
    jogadas[f'Jogador {i}'] = randint(1, 6)

ranking = sorted(jogadas.items(), key=itemgetter(1), reverse=True)

aux = 0
for i in range(0, 4):

    if i == 0:
        print(f'O {ranking[i][0]} ficou em {i + 1}º com {ranking[i][1]}')
        aux = i+1
    elif ranking[i][1] == ranking[i-1][1]:
        print(f'O {ranking[i][0]} ficou em {aux}º com {ranking[i][1]}')
    else:
        print(f'O {ranking[i][0]} ficou em {i + 1}º com {ranking[i][1]}')
        aux = i+1
    sleep(0.5)
