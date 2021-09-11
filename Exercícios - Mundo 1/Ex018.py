import math

ângulo = float(input('Digite um ângulo qualquer da circunferência trigonométrica: '))
rad = ângulo * math.pi/180
print('O seno do ângulo {}º será {:.3f}' .format(ângulo, math.sin(rad)))
print('O valor do cosseno será {:.3f}' .format(math.cos(rad)))
print('E a tangente será {:.3f}' .format(math.tan(rad)))
