n = list()
n2 = list()

while True:
    num = int(input('Digite um número: '))
    if num in n:
        print('Você já digitou esse número, digite outro!')
    else:
        n.append(num)
    opcao = str(input('Deseja continuar? [S/N]')).strip().lower()[0]
    if opcao in 'n':
        break
n2 = sorted(n)
print(f'Você digitou {len(n)} números e em ordem crescente eles ficam: {n2}')
