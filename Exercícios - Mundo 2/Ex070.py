nome = continuar = barato = ''
preço = .1
total = mais1000 = cont = 0
menor = -1

while True:
    print('-=' * 35)
    nome = str(input('Digite o nome do produto: ')).strip().lower().title()
    preço = float(input('Agora o preço: R$'))
    cont += 1

    total += preço
    if cont == 1:
        menor = preço
        barato = nome
    elif preço < menor:
        menor = preço
        barato = nome
    if preço > 1000:
        mais1000 += 1

    continuar = str(input('Deseja continuar digitando mais produtos? (S/N): ')).strip().lower()[0]
    if continuar == 'n':
        break
print('-=' * 35)
print(f'O valor total dos produtos será R${total:.2f}\n'
      f'você pagou mais de R$1000,00 em {mais1000} produtos\n'
      f'e o produto mais barato foi {barato}')
