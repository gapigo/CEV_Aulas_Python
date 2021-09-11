def fatorial(num):
    if num == 1:
        return num
    else:
        x = fatorial(num-1)
        return num*x


print(fatorial(4))