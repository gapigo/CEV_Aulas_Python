from random import choice

print('\033[33m' + '-=-' * 8 + '\033[33m')
print(' ' * 7 + 'JOKENPÔ!' + ' ' * 7)
print('\033[33m' + '-=-' * 8 + '\033[33m')
print('''\033[37mRegras: 
PAPEL ganha de PEDRA
PEDRA ganha de TESOURA
TESOURA ganha de PAPEL

digite "papel", "pedra" ou "tesoura": ''')
jogada = str(input('')).strip()
jogada = jogada.lower()
jogadas = ['papel', 'pedra', 'tesoura']
computador = choice(jogadas)

if jogada in jogadas:
    # Analisa as jogadas que vencem a partida
    if jogada == 'papel' and computador == 'pedra':
        print('\033[1;32mVocê venceu!')
    elif jogada == 'pedra' and computador == 'tesoura':
        print('\033[1;32mVocê venceu!')
    elif jogada == 'tesoura' and computador == 'pedra':
        print('\033[1;32mVocê venceu!')

    # Analisa as jogadas que perdem a partida
    elif jogada == 'papel' and computador == 'tesoura':
        print('\033[1;31mVocê perdeu.')
    elif jogada == 'tesoura' and computador == 'pedra':
        print('\033[1;31mVocê perdeu.')
    elif jogada == 'pedra' and computador == 'papel':
        print('\033[1;31mVocê perdeu.')

    # Analisa as jogadas que empatam a partida
    else:
        print('\033[1;33mO jogo empatou!')
else:
    print('\033[1;31m[ERROR 404] Valor não compreendido!')
