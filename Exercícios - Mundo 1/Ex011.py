print('Esse programa calcula o necessário de tinta para pintar tal área de uma parede')
h = float(input('Digite a altura da parede em metros: '))
l = float(input('Digite a largura da parede em metros: '))

v = (h*l)/2

print('\nA parede de {} e {} de {:.3f}m² precisa de {:.3f}L de tinta' .format(h, l, h*l, v))