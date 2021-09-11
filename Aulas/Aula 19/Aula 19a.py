pessoas = {'nome': 'Gustavo', 'sexo':'M', 'idade': 22}
print(pessoas['idade'])
print(f'O {pessoas["nome"]} tem {pessoas["idade"]}')
print(pessoas.keys())
print(pessoas.values())
print(pessoas.items())
for k, v in pessoas.items():
    print(f'{k} = {v}')
for k in pessoas.keys():
    print(k)
for v in pessoas.values():
    print(v)
del pessoas['sexo']
for k, v in pessoas.items():
    print(f'{k} = {v}')
pessoas['nome'] = 'Leandro'
pessoas['peso'] = 98.5
for k, v in pessoas.items():
    print(f'{k} = {v}')
    