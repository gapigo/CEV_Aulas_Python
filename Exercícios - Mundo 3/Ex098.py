from time import sleep

def contador(início, fim, passo):
    if passo < 0:
        p = passo * -1
    elif passo == 0:
        p = 1
    else:
        p = passo
    linha()
    print(f'Contagem de {início} até {fim} de {p} em {p}')
    if início < fim:
        while início <= fim:
            print(f'{início}, ', end='', flush=True)
            sleep(0.4)
            início += p
        print('Fim!')
    else:
        while fim <= início:
            print(f'{início}, ', end='', flush=True)
            sleep(0.4)
            início -= p
        print('Fim!')


def linha():
    print('-=' * 15)


# Corpo do programa

contador(1, 10, 1)
contador(10, 0, -2)
print('Agora é sua vez de personalizar a contagem!')
Início = int(input('Início: '))
Fim = int(input('Fim:    '))
Passo = int(input('Passo:  '))
contador(Início, Fim, Passo)
