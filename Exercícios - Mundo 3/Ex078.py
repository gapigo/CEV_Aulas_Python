números = list()
maiorpos = list()
menorpos = list()
maior = menor = 0

for c in range(0, 5):
    números.append(int(input(f'Digite o {c+1}º número: ')))
maior = max(números)
menor = min(números)
for c in range(0, 5):
    if números[c] == maior:
        maiorpos.append(c+1)
    if números[c] == menor:
        menorpos.append(c+1)

print('Você digitou 5 números')
print(f'O {menor} é o menor e aparece ', end='')
if len(menorpos) == 1:
    print(f'na {menorpos[0]}ª posição')
else:
    print(f' nas {menorpos}ª posições')
print(f'O {maior} é o maior e aparece ', end='')
if len(maiorpos) == 1:
    print(f'na {maiorpos[0]}ª posição')
else:
    print(f' nas {maiorpos}ª posições')
