def leiaDinheiro(mensagem):
    verificador = False
    while not verificador:
        num = str(input(mensagem)).strip()
        num = num.replace(' ', '')
        if num.count(',') == 0 and num.count('.') == 0:
            verificador = num.isnumeric()
        elif num.count(',') == 1:
            numeros = num.split(',')
            verificador = numeros[0].isnumeric() and numeros[1].isnumeric()
            num = num.replace(',', '.')
        elif num.count('.') == 1:
            numeros = num.split('.')
            verificador = numeros[0].isnumeric() and numeros[1].isnumeric()
        if verificador is False:
            print(f'\033[1;30;41mERRO! "{num}" é um preço inválido!\033[m')
    return float(num)
