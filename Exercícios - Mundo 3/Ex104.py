def leiaInt(mensagem):
    buffer = ''
    while not buffer.isnumeric():
        print(mensagem, end='')
        buffer = str(input('')).strip()
        if buffer.isnumeric():
            return int(buffer)
        else:
            print('\033[;31;mERRO! Digite um número inteiro válido.\033[;37;m')


n = leiaInt('Digite um número: ')
print(f'Você acabou de digitar o número {n}')
