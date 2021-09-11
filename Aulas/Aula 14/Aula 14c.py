r = bool(True)
while r:
    n = int(input('Digite um valor: '))
    controle = str(input('Quer continuar? [S/N]')).strip().lower()
    if controle == 'n':
        r = False
print('Fim')
