from random import shuffle
print('Escreva 4 nomes: ')
nome1 = input('Nome 1: ')
nome2 = input('Nome 2: ')
nome3 = input('Nome 3: ')
nome4 = input('Nome 4: ')

nomes = [nome1, nome2, nome3, nome4]

shuffle(nomes)

print('A ordem de chamada será {}' .format(nomes))
