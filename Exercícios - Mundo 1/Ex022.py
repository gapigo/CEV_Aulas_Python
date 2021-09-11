nome = str(input('Digite um nome completo: ')) .strip()

print('"{}" é o nome só em maiúsculas' .format(nome.upper()))

print('"{}" é o nome só em minúsculas' .format(nome.lower()))

print('Seu nome ao todo tem {} letras' .format(len(nome.replace(' ', ''))))

nomes = nome.split()

print('{} é o primeiro nome e ele tem {} letras' .format(nomes[0], len(nomes[0])))

