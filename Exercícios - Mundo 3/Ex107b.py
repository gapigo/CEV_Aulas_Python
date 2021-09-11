from Ex107a import aumentar, diminuir, dobro, metade

p = float(input('Digite o preço: R$'))
print(f'A metade de {p} é R${metade(p)}')
print(f'O dobro de {p} é R${dobro(p)}')
print(f'Aumentando 10%, temos R${aumentar(p, 10)}')
print(f'Reduzindo 13%, temos R${diminuir(p, 13)}')

