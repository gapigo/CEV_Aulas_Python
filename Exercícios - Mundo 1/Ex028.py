from random import randint

print('Programa de testar a sorte!')

número = randint(1, 5)

teste = int(input('Digite um número de 1 a 5 que você acha que o computador sorteou: '))

if teste == número:
    print('\nCaramba, você acertou o número, parabéns, 1/5 de chance')
else:
    print('\nProbabilisticamente, você não acertou. ')
    print('Eu pensei em {} e você em {}' .format(número, teste))
