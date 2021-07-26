numeroFatorial = int(input('Digite o número para ser fatorado: '))
fatorando = numeroFatorial
f = 1
print('{}! = '.format(numeroFatorial), end =' ')
while fatorando > 0:
    print('{}'.format(fatorando), end = ' ')
    print('X ' if fatorando > 1 else ' = ', end ='')
    f *= fatorando
    fatorando -= 1
print('{}'.format(f))
    