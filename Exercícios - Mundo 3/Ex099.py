from time import sleep


def maior(* numeros):
    m = numeros[0]
    print('-=' * 10)
    print('Analisando os valores: ', end='')
    for numero in numeros:
        print(f'{numero} ', end='', flush=True)
        sleep(0.25)
        if numero > m:
            m = numero
    print(f'\nEntre os números informados, {m} é o maior')


# Corpo do programa
maior(4, 7, 9, 1, 5, 12, 4, 7)
maior(5, 4, 5, 4, 54, 5, 4, 5, 45, 4524, 2, 2)
maior(4, 55, 4, 45, 45, 4, 5, 75, 76, 74, 423, 45, 2, 42, 45, 2, 53, 45, 23, 43, 45, 345, 3)
