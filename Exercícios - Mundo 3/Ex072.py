contagem = 'zero', 'um', 'dois', 'três', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove', 'dez', 'onze', 'doze', 'treze', \
           'catorze', 'quinze', 'dezesseis', 'dezessete', 'dezoito', 'dezenove', 'vinte'

while True:
    num = int(input('Digite um número inteiro entre 0 e 20: '))
    if 0 <= num <= 20:
        print(f'O número {num} por extenso é {contagem[num]}')
        break
    else:
        print('O número digitado foge dos parâmetros!')
