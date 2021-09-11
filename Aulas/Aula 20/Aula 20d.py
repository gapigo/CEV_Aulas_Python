def contador(*num):
    print(len(num))


def tela(*num):
    for valor in num:
        print(f'{valor} ', end='')
    print('FIM!')


def soma3(*num):
    x = 0
    for i in range(0, len(num)):
        x += num[i]
    print(x)


#corpo
soma3(5, 6, 7, 9, 10)
contador(5, 7, 1, 5)
tela(5, 4, 6)
tela(7, 9, 10)
tela(1,4,54,78,75,52,4,4,2,12,23,12,3,123,3,5,23,213,123,12,31,23,12,33,7)
