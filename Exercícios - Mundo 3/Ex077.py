tupla = 'python', 'mouse', 'computador', 'adesivo', 'impressora', 'mesa', 'teclado', 'monitor', 'caixa'
for c in tupla:
    print(f'A palavra {c.upper()} temos ', end='')
    for d in c:
        if d.lower() in 'aeiou':
            print(f'{d.lower()}', end=' ')
    print('\n', end='')
