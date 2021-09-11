ficha = dict()

ficha['nome'] = str(input('Digite seu nome: ')).strip().title()
ficha['ano de nascimento'] = int(input('Digite o ano de seu nascimento: '))
while True:
    ficha['verificação carteira'] = str(input('Tem carteira assinada? [S/N]')).strip().upper()[0]
    if ficha['verificação carteira'] not in 'SsNn':
        print(' >> DADO INVÁLIDO! TENTE NOVAMENTE! <<')
    else:
        break
if ficha['verificação carteira'] == 'S':
    ficha['verificação carteira'] = 'Sim'
    ficha['Ano de contratação'] = int(input('Digite o ano de contratação: '))
    ficha['Salário'] = float(input('Agora digite o salário: R$'))
    ficha['Idade que vai se aposentar'] = (ficha['Ano de contratação'] + 35) - ficha['ano de nascimento']
elif ficha['verificação carteira'] == 'N':
    ficha['verificação carteira'] = 'Não'

for k, v in ficha.items():
    print(f'{k.capitalize()}: {v.capitalize() if type(v) == str else v }')
