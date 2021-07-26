from time import sleep
resp = 'S'
quant = soma = maior = menor = 0 
while resp in 'Ss':
    numero = int(input('Digite um número: '))
    resp = str(input('Quer continuar? [S/N]\n').strip().upper()[0])
    soma += numero
    quant += 1
    if quant == 1:
        maior = numero
        menor = numero
    else:
        if numero > maior:
            maior = numero
        if numero < menor:
            menor = numero
media = soma/quant
print('Você digitou {} números, sua soma é {}'.format(quant,soma))
print('Sua média é {}, o maior número é {} e o menor {}'.format(media,maior,menor))
print('Acabou', end = '')
sleep(1)
print('.', end = '')
sleep(1)
print('.', end = '')
sleep(1)
print('.')
