valor = float(input('Digite o preço do produto: R$'))
print('(0 para à vista no dinheiro ou no cheque)\n(1 para à vista no cartão)')
par = int(input('Digite o número de parcelas que ele vai ser pago: '))

if par == 0:
    preço = 0.9*valor
elif par == 1:
    preço = 0.95*valor
elif par == 2:
    preço = valor
else:
    preço = 1.2*valor
print('\nO valor a ser pago será R${:.2f}' .format(preço), end=' ')
if par == 2:
    print('com 2x de R${:.2f}' .format(preço/2))
if par >= 3:
    print('COM JUROS em {}x de R${:.2f}.' .format(par, preço/par))
