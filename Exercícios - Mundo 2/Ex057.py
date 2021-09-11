sexo = 'teste'
while sexo not in 'MmFf':
    sexo = str(input('Digite o sexo de uma pessoa [F/M]: '))
    if sexo not in 'MmFf':
        print('Valor desconhecido, digite novamente (só pode F ou M)!!!')
print('Sexo {} registrado com sucesso!' .format(sexo.upper()[0]))
