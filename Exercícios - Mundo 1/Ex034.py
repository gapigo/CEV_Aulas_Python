sal = float(input('Quantifique o valor do salário: R$'))

if sal > 1250:
    novo = sal + 0.1*sal
else:
    novo = sal + 0.15*sal
print('O salário reajustado será R${:.2f}' .format(novo))

