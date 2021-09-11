soma = 0
for c in range(1, 501):
    if c % 2 == 1 and c % 3 == 0:
        soma += c

print('''A soma entre todos os números ímpares que são múltiplos 
de três e que se encontram no intervalo de 1 até 500 é igual a \033[1;31m{}''' .format(soma))
