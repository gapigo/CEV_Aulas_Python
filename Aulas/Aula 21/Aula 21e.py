def somar(a=0, b=0, c=0, d=0):
    return a+b+c+d


# Corpo do programa
r1 = somar()
r2 = somar(1)
r3 = somar(1, 2)
r4 = somar(1, 2, 3)
r5 = somar(1, 2, 3, 4)

print(f'A soma r1 vale {r1}\n'
      f'A soma r2 vale {r2}\n'
      f'A soma r3 vale {r3}\n'
      f'A soma r4 vale {r4}\n'
      f'A soma r5 vale {r5}\n')
