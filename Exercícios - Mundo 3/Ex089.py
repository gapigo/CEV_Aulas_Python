aluno = list()
escola = list()
media = 0

while True:
    aluno.append(str(input('Digite o nome do aluno: ')))
    aluno.append(float(input('Digite a nota 1: ')))
    aluno.append(float(input('Agora a nota 2: ')))
    opcao = str(input('Deseja continuar? [S/N]')).strip().lower()[0]
    escola.append(aluno[:])
    aluno.clear()
    if opcao in 'n':
        break
for i, v in enumerate(escola):
    if i == 0:
        print('=~' * 20)
        print('No. {:<30} MEDIA'.format('ALUNO'))
    media = (escola[i][1] + escola[i][2]) / 2
    print(f'{i}   {escola[i][0].strip().title():<30}  {media:>.1f}')
print('=~' * 20)
while True:
    r = int(input('Escolha o número de um aluno para ver as notas (-1 para não): '))
    if r == -1:
        break
    else:
        print(f'As notas de {escola[r][0]} são {escola[r][1]} e {escola[r][2]}')
    print('=~' * 20)
print('Obrigado e volte sempre!')
