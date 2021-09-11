from random import randint
print('PAR OU ÍMPAR! ESCOLHA UM NÚMERO E JOGUE PAR OU ÍMPAR [Par/Ímpar]')

jogada = True
n = computador = pontuação = 0
parouimpar = ''
while True:
    print('-='*30)
    n = int(input('Sua vez! Escolha um número: '))
    while True:
        parouimpar = str(input('Escolha! Par ou ímpar? ')).strip().lower()
        if parouimpar in 'par':
            jogada = True
            break
        elif parouimpar in 'ímparimpar':
            jogada = False
            break
        else:
            print('VALOR DESCONHECIDO! DIGITE NOVAMENTE!')
    computador = randint(0, 10)

    if ((computador + n) % 2 == 0) and jogada is True:
        print(f'Você venceu! O computador escolheu {computador} e o resultado total foi par!')
    elif ((computador + n) % 2 == 1) and jogada is False:
        print(f'Você venceu! O computador escolheu {computador} e o resultado total foi ímpar!')
    else:
        print(f'Você perdeu =(\nO computador escolheu {computador} e o resultado total foi', end='')
        if jogada is True:
            print(' ímpar')
        if jogada is False:
            print(' par')
        break
    pontuação += 1
print('-='*30)
print('Você fez {} ponto'.format(pontuação), end='s' if pontuação != 1 else '')
