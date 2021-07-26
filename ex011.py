largura = float(input('Digite a largura da parede:'))
altura = float(input('Digite a altura da parede:'))
area = largura * altura
print('A área de sua parede é {} e você precisa de {:.2f} litros de tinta para pintar'.format(area, area/2))