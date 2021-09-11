from datetime import date

ano = int(input('Digite o ano de nascimento: '))

idade = date.today().year - ano

if idade <= 9:
    print('A categoria desta idade será MIRIM')
elif idade <= 14:
    print('A categoria desta idade será INFANTIL')
elif idade <= 19:
    print('A categoria desta idade será JUNIOR')
elif idade <=25:
    print('A categoria desta idade será SÊNIOR')
else:
    print('A categoria desta idade será MASTER')
