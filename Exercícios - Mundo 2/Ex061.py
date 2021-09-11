n1 = int(input('Digite o primeiro termo da PA: '))
razão = int(input('Agora digite a razão da PA: '))
print('PA = [', end='')
c = 1
while c < 11:
    if c == 10:
        print('{}]' .format(n1 + (c-1)*razão))
    else:
        print('{}, '.format(n1 + (c-1)*razão), end='')
    c += 1

