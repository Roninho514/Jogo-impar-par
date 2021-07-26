PesoMaior = 0
PesoMenor = 0
for c in range(1,6):
    peso = float(input('Peso da {}ª pessoa: '.format(c)))
    if c == 1:
        PesoMaior = peso
        PesoMenor = peso
    else:
        if PesoMaior < peso:
            PesoMaior = peso
        elif PesoMenor > peso:
            PesoMenor = peso
print('O menor peso é {} e o maior {}'.format(PesoMenor, PesoMaior))
