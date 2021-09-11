nome = 'José'
idade = 33
print(f'O {nome} tem {idade} anos.') #PYTHON 3.6+
print('O {} tem {} anos'.format(nome, idade)) #PYTHON 3
print('O %s tem %d anos.' % (nome, idade)) # PYTHON 2

salário = 987.3
print(f'{nome} ganha R${salário:.2f}')
