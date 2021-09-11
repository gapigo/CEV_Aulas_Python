print('Digite 6 números: ')
soma = 0
for c in range(0, 6):
    num = int(input('-> '))
    if num % 2 == 0:
        soma += num
print('A soma dos números pares foi', soma)
