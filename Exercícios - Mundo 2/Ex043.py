print('\033[33m-=-'*11)
print('\033[35mPrograma para o cálculo do IMC')
print('\033[33m-=-'*11)
peso = float(input('Digite seu peso em Kg: '))
altura = float(input('Agora digite sua altura em metros: \033[m'))
imc = peso / (altura**2)

if imc < 18.5:
    print('\033[36mVocê está abaixo do peso')
elif 18.5 <= imc <= 25:
    print('\033[34mVocê está no peso ideal')
elif 25 < imc <= 30:
    print('\033[33mVocê está sobrepeso')
elif 30 < imc <= 40:
    print('\033[31mVocê está obeso')
elif imc > 40:
    print('\033[1;31mVocê está obeso mórbido')
