lista = list()
l5 = False
pos5 = list()

while True:
    num = int(input('Digite um número: '))
    lista.append(num)
    opcao = str(input('Deseja continuar? [S/N] ')).strip().lower()[0]
    if opcao in 'n':
        break
print(f'Você digitou {len(lista)} elementos')

for pos, atual in enumerate(lista):
    if atual == 5:
        l5 = True
        pos5.append(pos)
if l5 is True:
    if len(pos5) == 1:
        print(f'O número 5 está na lista e você o digitou na posição: {pos5[0]}')
    else:
        print(f'O número 5 está na lista e você o digitou nas posições: {pos5}')
else:
    print('Você não digitou o número 5')
lista.sort(reverse=True)
print(f'E a lista ordenada de forma decrescente é {lista}')
