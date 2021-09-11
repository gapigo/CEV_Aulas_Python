nome = str(input('Digite seu nome: ')).strip()
if nome.lower() == 'gabriel':
    print('Que nome bonito, Gabriel! ')
elif nome.lower() == 'pedro' or nome.lower() == 'maria':
    print('Seu nome é bem comum no Brasil. ')
elif nome.lower() in 'ana, cláudia, jéssica, juliana':
    print('Que belo feminino! ')
else:
    print('Que nome normal...')
print('Tenha um bom dia, {}. ' .format(nome.title()))

