expressão = str(input('Digite uma expressão matemática com parênteses: '))
pLeft = pRight = saldo = 0
letraPassada = 'a'

for letra in expressão:
    if letra == '(':
        pLeft += 1
    elif letra == ')':
        pRight += 1
saldo = pLeft - pRight
if saldo != 0:
    print('Os parênteses não foram fechados corretamente.')
else:
    certo = True
    for letra in expressão:
        if letraPassada in '.,' and letra in '(':
            certo = False
        if letraPassada in '+-/*.,' and letra in ')':
            certo = False
            print(f'{letraPassada} {letra}')
        letraPassada = letra
    if certo is not True:
        print('Cada parêntese tem seu correspondente, mas a expressão matemática descrita não faz sentido! ')
    else:
        print('Sua expressão é válida e corretíssima =)')
