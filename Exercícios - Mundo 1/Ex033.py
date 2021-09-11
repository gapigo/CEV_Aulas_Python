num1 = int(input('Digite o primeiro número: '))
num2 = int(input('Digite o segundo número: '))

if num1 < num2:
    menor = num1
    maior = num2
else:
    menor = num2
    maior = num1

num3 = int(input('Digite o terceiro número: '))

if num3 < menor:
    menor = num3
if num3 > maior:
    maior = num3

print('O maior número é {} e o menor é {}' .format(maior, menor))
