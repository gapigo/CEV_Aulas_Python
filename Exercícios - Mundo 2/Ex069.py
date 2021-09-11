idade = mais18 = homens = mulheres = 0
sexo = cadastrar = ''


while True:
    print('-='*35)
    idade = int(input('Digite a idade: '))
    while True:
        sexo = str(input('Agora o sexo (F/M): ')).strip().upper()[0]
        if sexo in 'FM':
            break
    if idade >= 18:
        mais18 += 1
    if sexo == 'M':
        homens += 1
    elif idade < 20:
        mulheres += 1
    cadastrar = str(input('Deseja cadastrar mais uma pessoa? (S/N): ')).strip().upper()[0]
    if cadastrar in 'N':
        print('-=' * 35)
        break
print(f'Existem {mais18} pessoa', end='s ' if mais18 != 1 else ' ')
print('maior', end='es ' if mais18 != 1 else ' ')
print('de 18 anos')
print(f'{homens} home', end='ns\n' if homens != 1 else 'm\n')
print(f'e {mulheres} mulher', end='es ' if mulheres != 1 else ' ')
print('menor', end='es ' if mulheres != 1 else ' ')
print('de 20 anos')

