produtos = 'Lápis', 1.5, 'Caneta', 2, 'Borracha', 3, 'Apontador', 5, 'Caderno', 20, 'Livro escolar', 119.99, \
           'Branquinho', 7.8, 'Apontador elétrico', 50

print('='*50)
for c in range(0, len(produtos), 2):
    print(f'{produtos[c]:.<41}R${produtos[c+1]: >7.2f}')
print('='*50)
