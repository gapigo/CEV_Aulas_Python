número = int(input('Digite um número de 0 a 9999: '))

print('Unidade: {}' .format(número % 10))
print('Dezena: {}' .format((número % 100) // 10))
print('Centena: {}' .format((número % 1000) // 100))
print('Milhar: {}' .format((número % 10000) // 1000))

