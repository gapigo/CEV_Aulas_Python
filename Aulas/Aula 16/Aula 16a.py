# Declaração de tuplas

lanche = ('Hambúrguer', 'Suco', 'Pizza', 'Pudim')
lanche2 = 'Hambúrguer', 'Suco', 'Pizza', 'Pudim'  # PYTHON 3.5
print(lanche)
print(lanche2[-1])
print(lanche2[1:3])
print(lanche[:2])
print(lanche[::])
print('----------------------')
for comida in lanche:
    print(comida)
print('======================')
for cont in range(0, len(lanche)):
    print(lanche[cont])
