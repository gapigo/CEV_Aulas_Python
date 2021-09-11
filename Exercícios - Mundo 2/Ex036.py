valor = float(input('Digite o valor da casa: R$'))
sal = float(input('Digite o valor do salário: R$'))
ano = int(input('Digite o valor de anos que se pretende quitar o empréstimo: '))

if 0.3*sal >= valor/(ano*12):
    print('O empréstimo foi \033[33mAPROVADO\033[m!')
    print('A parcela de R${:.2f} é o suficiente para você' .format(valor/(ano*12)))
else:
    print('O empréstimo foi \033[31mNEGADO\033[m!')
    print('Pois a parcela mensal seria de R${:.2f} e você só ganha R${:.2f}' .format(valor/(ano*12), sal))
    print('Você precisaria de pelo menos {:.0f} anos pra quitar a dívida' .format((valor/(0.3*sal))/12))
