n = 1
contapar = 0
totalpar = 0
contaimpar = 0
totalimpar = 0

while n != 0:
    n = int(input('Digite um número: '))

    if n != 0:
        if n % 2 == 0:
            contapar += 1
            totalpar += n
        else:
            contaimpar += 1
            totalimpar += n

print('Você digitou {} pares que somam {}.' .format(contapar, totalpar))
print('E digitou {} ímpares que somam {}.' .format(contaimpar, totalimpar))
