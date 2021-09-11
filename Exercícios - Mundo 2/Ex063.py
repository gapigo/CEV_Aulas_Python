n = int(input('Digite o número de termos da sequência Fibonacci que deseja ler: '))

i = 0
atual = 1
anterior = 0

while i < n:
    if i == 0:
        print('0 -> ', end='')
    else:
        if i == n - 1:
            print('{}' .format(atual), end='')
        else:
            print('{} -> '.format(atual), end='')
        aux = atual
        atual += anterior
        anterior = aux
    i = i + 1
