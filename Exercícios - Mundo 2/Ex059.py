opção = '4'

while opção != '5':

    if opção == '4':
        print('Calculadora! Digite 2 valores!')
        n1 = int(input('Digite o valor 1: '))
        n2 = int(input('Digite o valor 2: '))
    elif opção == '1':
        print('SOMADOR -> {}+{}={}' .format(n1, n2, n1 + n2))
    elif opção == '2':
        print('MULTIPLICADOR -> {}x{}={}' .format(n1, n2, n1*n2))
    elif opção == '3':
        maior = n1
        if n2 == n1:
            print('O maior número entre {} e {} é {} pois os 2 são iguais!!' .format(n1, n2, maior))
        elif n2 > maior:
            maior = n2
        print('O maior número de {} e {} é {}' .format(n1, n2, maior))

    else:
        print('VALOR DESCONHECIDO!!')
    print('''[1] somar            
[2] multiplicar      
[3] maior            
[4] novos números    
[5] sair do programa 
-==-==-==-==-==-==-==-==-''')
    opção = str(input('Agora escolha uma opção: ')).strip()
    print('-==-==-==-==-==-==-==-==-')
print('ATÉ LOGO! =)')
