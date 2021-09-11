números = list()
pares = list()
ímpares = list()

números.append(pares)
números.append(ímpares)

for c in range(0, 7):
    num = int(input(f'Digite o {c+1}º número: '))
    if num % 2 == 0:
        pares.append(num)
    else:
        ímpares.append(num)
ímpares.sort()
pares.sort()
print('=~'*30)
print(f'Os pares foram {números[0]}\nE os ímpares foram {números[1]}')
