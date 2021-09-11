print('Digite o peso de 5 pessoas em Kg:')
for c in range(0, 5):
    peso = float(input('Digite o {}º peso: ' .format(c+1)))
    if c == 0:
        maior = peso
        menor = peso
    else:
        if peso < menor:
            menor = peso
        if peso > maior:
            maior = peso
print('O maior peso digitado foi {}Kg\nE o menor foi {}Kg' .format(maior, menor))
