frase = str(input('Digite uma frase: ')).strip()

print('Número de vezes que aparece letra "A": {}' .format(frase.lower().count('a')))

print('Posição que ela aparece pela primeira vez: {}' .format(frase.lower().find('a') + 1))

print('Posição que ela aparece pela última vez: {}' .format(frase.lower().rfind('a') + 1))

