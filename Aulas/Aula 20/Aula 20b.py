def fatorial(num):
    if num == 1:
        return num
    else:
        x = fatorial(num-1)
        num = num * x
        return num



print(fatorial(994))
