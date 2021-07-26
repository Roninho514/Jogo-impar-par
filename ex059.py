n1 = int(input('Digite o primeiro número: '))
n2 = int(input('Digite o segundo número: '))
menu = False
while not  menu:
    print(30*'=')
    print('[1] Somar\n[2] Subtrair\n[3] Multiplicar\n[4]Dividir\n[5]Sair do programa')
    numero = int(input('O que você quer fazer com esses números?\n'))
    if numero == 1:
        print('{} + {} = {}'.format(n1, n2, n1+n2))
    elif numero == 2:
        print('{} - {} = {}'.format(n1, n2, n1-n2))
    elif numero == 3:
        print('{} x {} = {}'.format(n1, n2, n1 * n2))
    elif numero == 4:
        print('{} / {} = {}'.format(n1, n2, n1/n2))
    elif numero == 5:
        menu = True
    else:
        print('Você digitou errado, tente de novo: ')