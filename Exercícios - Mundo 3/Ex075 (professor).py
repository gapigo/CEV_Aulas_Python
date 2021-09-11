tupla = (int(input('Digite um primeiro valor: ')),
         int(input('Digite um segundo valor: ')),
         int(input('Digite um terceiro valor: ')),
         int(input('Digite um quarto valor: ')))
print(f'Você digitou os valores {tupla}')
print(f'O valor 9 apareceu {tupla.count(9)} vezes')
if 3 in tupla:
    print(f'O valor 3 apareceu na {tupla.index(3)}ª posição')
else:
    print('O valor 3 não foi digitado em nenhum momento')
print('Os valores pares digitados foram ', end='')
for n in tupla:
    if n % 2 == 0:
        print(n, end=' ')
