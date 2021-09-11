def notas(*n, sit=False):
    """
    :param n: notas tipo float ou int para serem adicionadas
    :param sit: variável booleana que escolhe se o dicionário usará a key situação
    (mairo que 7 para bom, entre 5 até 7 para razoável e abaixo de 5 para ruim)
    :return: dicionário arrumado
    """
    r = dict()
    r['total'] = len(n)
    r['maior'] = max(n)
    r['menor'] = min(n)
    r['média'] = sum(n) / r['total']
    if sit == True:
        if r['média'] >= 7:
            r['situação'] = 'BOM'
        elif r['média'] >=5:
            r['situação'] = 'RAZOÁVEL'
        else:
            r['situação'] = 'RUIM'
    return r


# Programa principal

print(notas(6, 10, 7, 3.3, sit=True))
