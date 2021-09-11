início = int(input('Digite o número que começa a contagem: '))
fim = int(input('Digite o número que a contagem termina: '))
passo = int(input('Digite o passo: '))

for c in range(início, fim + 1, passo):
    print(c, end='\n')
