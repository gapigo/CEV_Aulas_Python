print('Programa de cálculo da condição do triângulo')
r1 = float(input('Digite a reta 1: '))
r2 = float(input('Digite a reta 2: '))
r3 = float(input('Digite a reta 3: '))

if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
    print('O triângulo {}, {}, {} existe'.format(r1, r2, r3))
else:
    print('As retas {}, {}, {} não conseguem formar um triângulo'.format(r1, r2, r3))
