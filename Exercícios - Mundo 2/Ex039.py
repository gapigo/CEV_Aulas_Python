from datetime import date
sexo = str(input('Qual é seu sexo (F/M)? ')).strip()

if sexo.upper() == 'M':

    ano = int(input('Qual é a seu ano de nascimento? '))

    idade = date.today().year - ano

    if idade < 18:
        print('Você ainda vai se alistar.\nFaltam {} ano(s)' .format(18 - idade), end='')
        print(' e você se alistará em {}' .format(ano + 18))
    elif idade == 18:
        print('Já é hora de se alistar!')
    elif idade > 18:
        print('Que bom! Você já passou da hora de se alistar.\nFizeram {} anos' .format(idade - 18), end='')
        print(' e você se alistou em {}' .format(ano + 18))
elif sexo.upper() == 'F':
    print('Você é mulher, não precisa fazer alistamento militar obrigatório')
else:
    print('Meu caro usuário, digitastes errado! Tente novamente.')
