a = [2, 3, 4, 7]
b = a
b[2] = 8
print(f'Lista A: {a}')
print(f'Lista B: {b}')

b = a[:]
a[2] = 4
print(f'Lista A: {a}')
print(f'Lista B: {b}')
