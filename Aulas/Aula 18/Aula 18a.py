teste = list()
teste.append('Gustavo')
teste.append(40)

galera = list()
galera.append(teste[::])  # TOMAR CUIDADO COM O ::

teste[0] = 'Maria'
teste[1] = 22

galera.append(teste[::])  # SE NÃO SE CRIA UMA LIGAÇÃO ENTRE AS LISTAS

print(galera)
