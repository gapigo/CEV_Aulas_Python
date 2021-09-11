print('{:=^40}' .format(' Programa de tabuada! '))
n = int(input('Digite o número que se deseja calcular a tabuada: '))
for c in range(1, 11):
    print('{}x{}={}' .format(n, c, c*n))
