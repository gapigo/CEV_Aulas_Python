from random import randint
from time import sleep


def sorteia(lista):
    print('Sorteando os 5 valores da lista: ', end='')
    for cont in range(0, 5):
        n = randint(0, 1000)
        lista.append(n)
        sleep(0.25)
        print(f'{n} ', end='', flush=True)
    print('', end='\n')


def par(lista):

    soma = 0
    for valor in lista:
        if valor % 2 == 0:
            soma += valor
    print(f"A somatória dos valores pares de {lista} é {soma}")


# Corpo do programa
lista = []
sorteia(lista)
par(lista)
