distancia = float(input('Digite a distância da viagem:'))
if distancia > 200:
    print('Você deve pagar: R${}'.format(distancia * 0.45))
else:
    print('Você deve pagar: R${}'.format(distancia * 0.50))
