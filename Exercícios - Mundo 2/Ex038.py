print('Digite dois valores: ')
num1 = int(input('Valor 1: '))
num2 = int(input('Valor 2: '))

if num1 == num2:
    print('Não existe valor maior, os dois são iguais.')
elif num1 > num2:
    print('O primeiro valor é maior')
elif num2 > num1:
    print('O segundo valor é maior')
