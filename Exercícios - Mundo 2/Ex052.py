num = int(input('Digite um número inteiro: '))
q = bool(True)
for c in range(2, num):
    if num % c == 0:
        q = False
if q:
    print('O valor digitado é primo!')
else:
    print('O valor digitado é comum.')
