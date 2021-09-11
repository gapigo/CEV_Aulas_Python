contador = 1
n1 = 0
razão = 0
opção = 'Sdasd'
while opção.lower() not in 'sairleavequitexitquitaresc':
    n1 = int(input('Digite o primeiro termo da PA: '))
    razão = int(input('Agora digite a razão da PA: '))
    números = int(input('Agora digite quantos números deseja mostrar: '))
    print('PA = [', end=' ')
    while contador != números:
        if contador == números - 1:
            print('{} ]' .format(n1 + (contador-1)*razão), end='\n')
        else:
            print('{}, '.format(n1 + (contador-1)*razão), end='')
        contador = contador + 1
    print('Digite "sair" para fechar o programa, ou aperte qualquer tecla pra continuar')
    opção = str(input('-> ')).strip()
