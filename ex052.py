print(50*'=')
print('Número Primo'.upper())
print(50*'=')
cont = 1
verificador = 0
numero = int(input('Digite um número: '))
for cont in range(1,numero):
    if numero%cont == 0:
        verificador = verificador + 1
        print('\033[32m{}'.format(cont), end=' ')
    else:
        print('\033[31m{}'.format(cont), end=' ')
    cont = cont + 1
print('')
if verificador > 2:
    print('Esse número não é primo!')
else:
    print('Esse número é primo! foi divisivel somente {}'.format(verificador))