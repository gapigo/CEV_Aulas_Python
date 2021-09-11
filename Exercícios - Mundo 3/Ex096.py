def área(largura, comprimento):
    área = largura*comprimento
    print(f'Um terreno {largura}m x {comprimento}m tem {área}m²')


def título(str):
    print(str)
    print('-' * len(str))


# Começo do programa

# área(8.6, 6)
# área(7, 9)

título('Controle de terrenos')
largura = float(input('Digite a largura (m): '))
comprimento = float(input('Digite o comprimento (m): '))
área(largura, comprimento)
