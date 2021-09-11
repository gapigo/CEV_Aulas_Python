from datetime import date

print('Digite o ano de nascimento de sete pessoas: ')

atual = date.today().year

menores = 0
maiores = 0
for c in range(0, 7):
    ano = int(input('Digite o {}º ano: '.format(c+1)))
    idade = atual - ano
    if idade < 21:
        menores += 1
    elif idade >= 21:
        maiores += 1
print('Existem {} pessoas menores que 21 anos' .format(menores))
print('E existem {} pessoas maiores de idade' .format(maiores))


