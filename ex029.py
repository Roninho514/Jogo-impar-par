velo = float(input('Digite a velocidade do carro:'))
if velo>80:
    print('Ele será multado.Terá que pagar R${}'.format((velo-80)*7.00))
else:
    print('Passou')
