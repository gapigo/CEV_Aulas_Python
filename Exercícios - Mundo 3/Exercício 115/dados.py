from cores import cor

def lerInt(mensagem):
    while True:
        try:
            buffer = str(input(mensagem)).strip().lower().replace(' ', '')
            num = int(buffer)
        except KeyboardInterrupt:
            cor('\nUsuário preferiu não digitar.', 'red', pularLinha=True)
        except:
            cor('Dado inválido!', 'red', pularLinha=True)
        else:
            return num


def lerFloat(mensagem):
    while True:
        try:
            buffer = str(input(mensagem)).strip().lower().replace(',', '.').replace(' ', '')
            num = float(buffer)
        except:
            cor('Dado inválido!', 'red', pularLinha=True)
        else:
            return num
