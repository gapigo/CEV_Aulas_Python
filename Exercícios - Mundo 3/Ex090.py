aluno = dict()
aluno['Nome'] = str(input('Digite o nome do aluno: ')).strip().title()
aluno['Media'] = float(input('Digite a média dele: '))
aluno['Situação'] = '?'
if aluno['Media'] >= 7:
    aluno['Situação'] = 'Aprovado'
elif aluno['Media'] >= 5:
    aluno['Situação'] = 'Recuperação'
else:
    aluno['Situação'] = 'Reprovado'
print(f'{aluno["Nome"]} foi {aluno["Situação"]}')
