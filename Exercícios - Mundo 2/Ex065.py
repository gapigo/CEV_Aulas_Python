n = soma = maior = menor = quantidade = 0
opção = 'S'

while opção not in 'Nn':
    n = int(input('Digite um número: '))
    if quantidade == 0:
        maior = n
        menor = n
    else:
        if n > maior:
            maior = n
        elif n < menor:
            menor = n
    quantidade += 1
    soma = soma + n
    opção = str(input('Deseja continuar? [S/N] ')).strip()

print('A média entre os {} números foi de {:.1f}' .format(quantidade, soma/quantidade))
print('e o menor número foi {} enquanto o maior foi {}' .format(menor, maior))
