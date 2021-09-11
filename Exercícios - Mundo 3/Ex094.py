ficha = dict()
pessoas = list()
mulheres = list()
acima = list()
soma = 0
while True:
    ficha['Nome'] = str(input('Digite o nome: ')).strip().title()
    ficha['Idade'] = int(input('Digite a idade: '))
    while True:
        ficha['Sexo'] = str(input('Agora digite o sexo: [F/M] ')).strip().lower()[0]
        if ficha['Sexo'] in 'FfMm':
            if ficha['Sexo'] in 'f':
                ficha['Sexo'] = 'Feminino'
            elif ficha['Sexo'] in 'm':
                ficha['Sexo'] = 'Masculino'
            break
        else:
            print('Valor incorreto, tecle novamente!')
    pessoas.append(ficha.copy())
    ficha.clear()
    opc = str(input('Deseja continuar a cadastrar? [S/N]')).strip().lower()[0]
    if opc in 'n':
        break
print(f'Ao total foram cadastradas {len(pessoas)} pessoas')
for pessoa in pessoas:
    soma += pessoa['Idade']
media = soma/len(pessoas)
print(f'A média das idades é {media}')
for pessoa in pessoas:
    if pessoa['Sexo'] in 'Feminino':
        mulheres.append(pessoa['Nome'])
    if pessoa['Idade'] > media:
        acima.append(pessoa['Nome'])
print(f'A lista das mulheres cadastradas é: ')
for mulher in mulheres:
    print(f'{mulher}; ', end='')
print(f'\nA lista das pessoas com idades maiores que a média é: ')
for pessoa in acima:
    print(f'{pessoa}; ', end='')
