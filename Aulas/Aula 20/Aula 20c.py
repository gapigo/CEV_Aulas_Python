def soma(num1, num2):
    return num1 + num2


def soma2(num1, num2):
    print(f'{num1} + {num2} = {num1+num2}')


def soma3(num1, num2, num3):
    if num3 is None:
        return num1 + num2
    else:
        return num1 + num2 + num3


# corpo
print(soma(8, 9))
print(soma(2, 1))
soma2(123, 51)
soma3(4, 6)

