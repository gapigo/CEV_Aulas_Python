from random import choices

print('Escreva 4 nomes: ')
nome1 = input('Nome 1: ')
nome2 = input('Nome 2: ')
nome3 = input('Nome 3: ')
nome4 = input('Nome 4: ')

nomes = [nome1, nome2, nome3, nome4]

print('O nome escolhido foi: {}' .format(choices(nomes, k=1)))
