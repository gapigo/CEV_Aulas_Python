from random import randint

numero = randint(0, 1000000)

print('Sou seu computador, acabei de pensar em um número entre 0 e 1 000 000, tente adivinhar!')

tentativas = 0
chute = 0

while chute != numero:
    chute = int(input('-> '))
    if chute != numero:
        if numero < chute:
            print('Menos!')
        else:
            print('Mais!')
    tentativas += 1
print('Parabéns, você acertou em {} tentativas' .format(tentativas))
