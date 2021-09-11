tupla = (int(input('Digite um primeiro valor: ')),
         int(input('Digite um segundo valor: ')),
         int(input('Digite um terceiro valor: ')),
         int(input('Digite um quarto valor: ')))
n9 = pos3 = npar = 0
ntem3 = True

for c in range(0, 4):
    if tupla[c] == 9:
        n9 += 1
    if tupla[c] %2 == 0:
        npar += 1
    if tupla[c] == 3:
        ntem3 = False
        pos3 = c
print(f'O número 9 aparece {n9} vezes')
if ntem3 is True:
    print('O número 3 não aparece na tupla')
else:
    print(f'O número 3 aparece na {tupla.index(3)+1}ª posição')
print(f'Há {npar} números pares')
