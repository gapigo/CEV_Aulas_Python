print('Programa que calcula a existência de um triângulo')
r1 = float(input('Digite a reta 1: '))
r2 = float(input('Digite a reta 2: '))
r3 = float(input('Digite a reta 3: '))
if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
    print('O triângulo existe e será: ', end='')
    if r1 == r2 == r3:
        print('\033[1;35mEQUILÁTERO')
    elif r1 == r2 or r1 == r3 or r2 == r3:
        print('\033[1;34mISÓSCELES')
    else:
        print('\033[1;32mESCALENO')

else:
    print('As retas {}, {} e {} não formam um triângulo.' .format(r1,  r2, r3))
