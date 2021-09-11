def notas(*num, sit=False):

    d = dict()
    d['Total'] = len(num)
    soma = 0
    for i in range(0, d['Total']):
        if i == 0:
            d['Maior'] = num[i]
            d['Menor'] = num[i]
        elif num[i] > d['Maior']:
            d['Maior'] = num[i]
        elif num[i] < d['Menor']:
            d['Menor'] = num[i]
        soma += num[i]
    d['Média'] = soma / d['Total']

    if sit is True:
        if d['Média'] < 5:
            d['Situação'] = 'Ruim'
        elif d['Média'] < 7:
            d['Situação'] = 'Razoável'
        else:
            d['Situação'] = 'Bom'
    return d


resp = notas(10, 5, 7, 6, sit=True)
print(resp)
