frase = str(input('Escreva uma frase: ')).strip()

aux = frase.lower().replace(' ', '')
aux2 = ''
tamanho = len(aux)

for c in range(0, tamanho):

    aux2 = aux2 + aux[tamanho-1-c]

if aux2 == aux:
    print('A frase escrita é um palíndromo!!!')
else:
    print('A frase escrita não tem nada demais...')

