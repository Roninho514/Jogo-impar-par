quantNumero = 0
somaNumero = 0
numero = 0
while numero != 999:
    numero = int(input('Digite [999] para parar: '))
    if numero != 999:
        somaNumero = numero + somaNumero
        quantNumero += 1
print('Você digitou {} números e a soma deles é {} '.format(quantNumero,somaNumero))