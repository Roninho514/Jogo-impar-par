print('==========Lojas Roni===============')
preco =float(input('Digite o preço do produto: '))
print('Formas de pagamento\n [1] A vista no dinheiro \n [2] A vista no cartão \n [3] Parcelado')
formaPag = int(input('Digite o número com base na forma de pagamento: '))
if formaPag == 1:
    print('O preço com será {} com os 10%  de desconto'.format(preco - ((preco*10)/100)))
elif formaPag == 2:
   print('O preço com será {} com os 5%  de desconto'.format(preco - ((preco*5)/100))) 
elif formaPag == 3:
    parcela = int(input('Quantas parcelas?\n'))
    if parcela >= 3:
        print('O preço será de {} por mês mais os 25% de juros'.format((preco + (preco*25)/100)/parcela))
    else:
        print('O preço ficará {} por mês'.format(preco/parcela))
else:
    print('Você digitou alguma tecla errada')
