from random import sample
from time import sleep
jogo = list()
jogadas = list()
num = int(input('Digite o número de jogos desejados: '))
print('=~'*16)
for i in range(0, num):
    jogo = sample(range(60), 6)
    jogo.sort()
    for j in range(0, 6):
        jogo[j] += 1
    jogadas.append(jogo[:])
    jogo.clear()
    print(f'Jogo {i+1}: {jogadas[i]}')
    sleep(0.7)
print('=~'*15)
