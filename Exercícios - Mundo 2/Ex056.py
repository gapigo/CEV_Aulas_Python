print('Escreva o nome, idade e sexo de quatro pessoas: ')
somaidades = 0
maioridade = 0
maisvelho = ''
countmeninas = 0
for contador in range(1,5):
    print('-'*5,'{}ªpessoa'.format(contador),'-'*5)
    nome = str(input('Escreva o nome: '))
    idade = int(input('Agora dê a idade de {}: ' .format(nome)))
    sexo = input('Agora o sexo (F/M): ')
    somaidades += idade
    if sexo.lower() == 'm':
        if idade > maioridade:
            maisvelho = nome
    if sexo.lower() == 'f' and idade < 20:
        countmeninas += 1

print('A média das idades das pessoas acima é {} anos' .format(somaidades/4))
print('O homem mais velho é o {} com {} anos' .format(maisvelho, maioridade))
print('E há {} meninas abaixo de 20 anos' .format(countmeninas))