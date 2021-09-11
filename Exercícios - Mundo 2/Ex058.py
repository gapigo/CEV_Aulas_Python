from random import randint

print('-='*10, end=' ')
print('JOGO DA ADIVINHAÇÃO!!', end=' ')
print('-='*10, end='\n')
print('Escolha um número que você acha que o computador escolheu! \n')
jogador = -1
computador = 0
npalpites = 0
while jogador != computador:
    computador = randint(1, 10)
    jogador = int(input('Digite seu palpite: '))
    npalpites += 1
    if computador != jogador:
        print('Errado, o computador "pensou" {} e você {}' .format(computador, jogador))
if npalpites == 1:
    print('Garaiu bixo, ustedes és um cagado, você digitou {} e o computador também!' .format(jogador))
else:
    print('Você ganhou! PARABÉNS!\nAo todo foram necessários {} palpites para você vencer com a jogada {}'
          .format(npalpites ,jogador))
