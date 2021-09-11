times = 'Palmeiras', 'Flamengo', 'Internacional', 'Grêmio', 'São Paulo', 'Atlético - MG', 'Atlético - PR', 'Cruzeiro', \
        'Botafogo', 'Santos', 'Bahia', 'Fluminense', 'Corinthians', 'Chapecoense', 'Ceará', 'Vasco', 'Sport', \
        'América', 'Vitória', 'Paraná'

print('Os primeiros cinco colocados são: ', end='')
for c in range(0, 5):
    print(f'{times[c]}', end=', ' if c != 4 else '')

print('\nOs últimos quatro colocados são: ', end='')
for c in range(1, 5):
    print(f'{times[-c]}', end=', ' if c != 4 else '')

print('\nOs times da tabela em ordem alfabética são:')
print(sorted(times))
print(f'E o time da chapecoense está na {times.index("Chapecoense")+1}ª posição')
