valor = c50 = c20 = c10 = c1 = resto = 0
continuar = ''

while True:
    print('-~'*20)
    valor = float(input('Qual é o valor? R$'))

    c50 = valor // 50
    resto = valor % 50

    c20 = resto // 20
    resto %= 20

    c10 = resto // 10
    resto %= 10

    c1 = resto // 1

    if c50 != 0:
        print(f'Serão {c50:.0f} cédulas de R$50')
    if c20 != 0:
        print(f'{c20:.0f} cédulas de R$20')
    if c10 != 0:
        print(f'{c10:.0f} cédulas de R$10')
    if c1 != 0:
        print(f'e {c1:.0f} cédulas de R$1')

    continuar = str(input('Digitar mais um valor? [S/N]: ')).strip().lower()[0]

    if continuar == 'n':
        break
print('-~'*20)
print('FIM!')
