nome = input('Digite um nome completo: ')

y = nome.find(' ')

x = nome.rfind(' ')

print('O primeiro nome é: {}' .format(nome[:y]))

print('O último nome é: {}' .format(nome[x+1:]))

'''

nome = input('Digite um nome completo: ')

lista = nome.split()

print('O primeiro nome é: {}' .format(lista[0]))

print('O último nome é: {}' .format(lista[len(lista)-1]))

'''