cont = 0
soma = 0
for cont in range(0,501):
    if cont%3 == 0 and cont%2 != 0:
        soma = cont + soma
print('A soma dos números impares multiplos de 3 é de {} '.format(soma))
