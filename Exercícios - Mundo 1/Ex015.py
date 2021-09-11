d = float(input('Quantos Km o carro alugado percorreu? '))
t = int(input('Quantos dias o carro foi alugado? '))

c = d*0.15 + t*60

print('O custo do aluguel será de R${:.2f}' .format(c))
