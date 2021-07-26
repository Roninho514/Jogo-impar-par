from random import randint
numero = randint(0,5)
resp = int(input('Digite o número que o computador pensou:'))
if numero == resp:
    print('Parabéns você acertou!')
else:
    print('Que pena você errou feio!! errou rude')
