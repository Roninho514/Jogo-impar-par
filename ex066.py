infinito = True
quantNumero = 0
soma = 0
while infinito == True:
    numero = int(input('Digite [999] para parar : '))
    if numero == 999:
        break
    quantNumero += 1
    soma += numero
print(f'Você digitou {quantNumero} e a soma é de {soma}')
