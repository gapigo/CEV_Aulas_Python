n = int(input('Digite um número que deseja-se calcular o fatorial: '))
c = 0
f = 1
print('{}! ='.format(n), end=' ')
while c != n:
    f = f * (n-c)
    if c == n-1:
        print('{}' .format(n-c), end='')
    else:
        print('{}x' .format(n-c), end='')
    c += 1
print(' = {}'.format(f))
