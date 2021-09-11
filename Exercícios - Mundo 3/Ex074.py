from random import randint

tupla = (randint(0, 10), randint(0, 10), randint(0, 10),
         randint(0, 10), randint(0, 10))

print('Os números sorteados foram: ', end='')
for pos, c in enumerate(tupla):
    print(f'{c}', end=', ' if pos != 4 else '')
print('\nO maior valor foi {} e o menor {}'.format(max(tupla), min(tupla)))
