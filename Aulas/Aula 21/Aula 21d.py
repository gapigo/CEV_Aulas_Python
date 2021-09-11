def teste():
    n1 = 4
    print(f'n1 dentro de teste vale {n1}')


def teste2():
    global n1
    n1 = 3
    print(f'n1 dentro de teste2 vale {n1}')

# Começo do programa
n1 = 1
teste()
print(f'n1 fora de teste vale {n1}')
teste2()
print(f'n1 fora de teste2 vale {n1}')
