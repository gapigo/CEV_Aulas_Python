frase = 'Curso em Vídeo Python'

lista = frase.split()  # Dividiu-se a frase em 4 objetos de um vetor

print(lista[2])  # Mandou-se escrever o terceiro objeto da lista (começa em 0 a contagem)

print(lista[0][2])  # Mandou-se escrever o 'r' de "curso"

colada = '='.join(lista)

print(colada)
