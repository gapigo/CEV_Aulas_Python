r = int(input('Digite a razão de uma PA: '))
n1 = int(input('Digite o primeiro elemento desta: '))
print('PA: [', end='')
for c in range(0, 10):
    n = n1 + r*c
    if c != 9:
        print('{}, '.format(n), end='')
    else:
        print('{}]' .format(n))

