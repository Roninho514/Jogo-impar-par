print(50*('='))
print('Tabuada')
print(50*('='))
cont = 1
num = int(input('Digite um número inteiro:'))
for cont in range(1,11):
    print('{} x {} = {}'.format(num, cont, num * cont))
