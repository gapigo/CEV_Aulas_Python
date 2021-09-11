def escreva(str):
    print('~' * (len(str) + 4))
    print(f'  {str}  ')
    print('~' * (len(str) + 4))


# Começo do programa

verificador = True
while verificador:
    escreva(input('Escreva algo: '))
    leitor = str(input('Deseja continuar? (Escreva Sim) ')).lower().strip()
    if leitor not in 'sim claro quero por favor':
        verificador = False
