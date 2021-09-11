número = int(input('Digite um número inteiro em decimal: '))
opção = str(input('''Agora digite uma opção para conversão: 
1 - Para binário
2 - Para octal
3 - Para hexadecimal
->''')).strip()

if opção == '1':
    convertido = bin(número)
    print('O número {} (decimal) em binário será {}' .format(número, convertido[2:]))
elif opção == '2':
    convertido = oct(número)
    print('O número {} (decimal) em octal será {}' .format(número, convertido[2:]))
elif opção == '3':
    convertido = hex(número)
    print('O número {} (decimal) em hexadecimal será {}' .format(número, convertido[2:]))
else:
    print('Caro usuário retardado, creio que não digitastes a opção correta. ')
    exit()
