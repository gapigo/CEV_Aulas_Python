i = 0
n = 0
soma = 0
print("Digite '999' para parar")
while n != 999:
    n = int(input('Digite o {}º número: '.format(i+1)))
    if n != 999:
        soma += n
        i += 1
print('Você digitou {} números e a soma total foi {}' .format(i, soma))
