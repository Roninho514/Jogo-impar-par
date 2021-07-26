from random import randint
computador = randint(0, 10)
print(7*'=', 'Adivinhação', 7*'=')
print('Sou seu computador e pensei em um número...\n Tente advinhar')
acertou = False
while not acertou:
    numeroJogador = int(input('É o número: '))
    if numeroJogador == computador:
        acertou = True
    elif numeroJogador < computador:
        print('Mais...')
    elif numeroJogador > computador:
        print('Menos')
print('Parabéns você acertou!!!!! é o número {}'.format(computador))