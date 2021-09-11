def fatorial(num, show):
    global var, primeiro
    if primeiro is True:
        var = num
        primeiro = False
    if num == 1:
        if show is True:
            print('1 ', end='')
        return num
    else:
        x = fatorial(num-1, show)
        if show is True:
            print(f'x {num} ', end='')
            if num == var:
                print('= ', end='')
        return x*num


def fat(num, show):
    """
    fat calcula o fatorial de um numero num
    :param int num: seleciona o número a ser calculado
    :param bool show: aponta se mostrará o processo a ser calculado ou não
    :return: retorna a função fatorial
    """
    global var
    global primeiro
    var = 0
    primeiro = True
    return fatorial(num, show)


# Começo do programa
print(fat(6, True))
print(fat(7, False))
help(fat)
