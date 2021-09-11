pessoa = list()
galera = list()
menor = maior = 0

while True:
    pessoa.append(str(input('Digite o nome: ')).strip().title())
    pessoa.append(float(input('Digite a seu peso: ')))
    galera.append(pessoa[:])
    pessoa.clear()
    opcao = str(input('Deseja continuar? [S/N] ')).strip().lower()[0]
    if opcao in 'n':
        break
print(f'Foram cadastradas {len(galera)} pessoas no total')
print(f'As pessoas mais leves foram: ', end='')
for c in range(0, len(galera)):
    if c == 0:
        maior = galera[c][1]
        menor = galera[c][1]
    elif galera[c][1] > maior:
        maior = galera[c][1]
    elif galera[c][1] < menor:
        menor = galera[c][1]
for c in range(0, len(galera)):
    if galera[c][1] == menor:
        print(f'{galera[c][0]};', end='')
print('\nAs pessoas mais pesadas: ', end='')
for c in range(0, len(galera)):
    if galera[c][1] == maior:
        print(f'{galera[c][0]};', end='')
