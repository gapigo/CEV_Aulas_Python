from time import sleep

print('\033[1;31;43m-=-'*16+'\033[m')
print('\033[1;31;43mPrograma de contagem regressiva para o ano novo \033[m')
print('\033[1;31;43m-=-'*16+'\033[m')

input('Aperte uma tecla para continuar: ')

for c in range(10, 0, -1):
    print('\033[1;4;32m{}' .format(c))
    sleep(1)
print('\033[1;35mFeliz ano novo!!!')
