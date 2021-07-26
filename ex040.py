primeiroBimestre = float(input('Digite sua nota do primeiro bimestre: '))
segundoBimestre = float(input('Digite sua nota do segundo bimestre: '))
media = (primeiroBimestre + segundoBimestre)/2
if media < 5:
    print('Sua média foi {}, você foi reprovado'.format(media))
elif media >= 5 and media <= 6.9:
    Print('Sua média foi {}, você está de recuperação'.format(media))
else:
    print('Sua média foi {}, você foi aprovado'.format(media))
