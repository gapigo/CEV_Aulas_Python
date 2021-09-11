d = float(input('Digite a distância da viagem percorrida (em Km): '))

if d <= 200:
    c = 0.5*d
else:
    c = 0.45*d
print('O custo da viagem, por ser {:.1f}km, será de R${:.2f}.' .format(d, c))
