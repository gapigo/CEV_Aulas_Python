def leiaInt(mensagem):
    while True:
        try:
            buffer = input(mensagem)
            num = int(buffer)
        except KeyboardInterrupt:
            print(f'\nO usuário preferiu não digitar nada')
            return 0
        except:
            print(f'O dado "{buffer}" não é um número inteiro! ')
        else:
            return num


def leiaFloat(mensagem):
    while True:
        try:
            buffer = str(input(mensagem)).strip().replace(',', '.').replace(' ', '')
            num = float(buffer)
        except KeyboardInterrupt:
            print(f'\nO usuário preferiu não digitar nada')
            return 0
        except:
            print(f'O dado "{buffer}" não é um número real!')
        else:
            return num


x = leiaInt('Digite um número inteiro: ')
y = leiaFloat('Agora digite um número real: ')
print(f'Parabéns, você digitou corretamente os números {x} e {y}')
