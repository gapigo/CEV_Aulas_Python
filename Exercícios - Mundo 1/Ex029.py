v = float(input('Velocidade do carro na hora da multa: '))

if v>80:
    c = (v-80) * 7
    print('Por passar com {:.1f}Km/h em uma estrada de 80Km/h, você pegou uma multa de R${:.2f}' .format(v, c))
else:
    print('Respeitando as leis do trânsito, você não pegou nenhuma multa, PARABÉNS!')
