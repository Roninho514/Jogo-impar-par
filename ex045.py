from random import randint
from time import sleep
itens = ['Pedra', 'Papel', 'Tesoura']
computador = randint(0, 2)
print('{}'.format(50*'-'))
print('Jokempo')
print('{}'.format(50*'-'))
print("""Suas opções
[0] Pedra
[1] Papel
[2] Tesoura""")
jogador = int(input('Escoha sua opção: '))
print('JO!')
sleep(2)
print('KEM!')
sleep(2)
print('PO!')
print('Computador escolheu {}'.format(itens[computador]))
print('Você escolheu {}'.format(itens[jogador]))
if computador == 0:
    if jogador == 0:
        print('EMPATE!')
    elif jogador == 1:
        print('Você ganhou!')
    elif jogador == 2:
        print('Você perdeu!')
    else:
        print('Jogada invalida')
elif computador == 1:
    if jogador == 0:
        print('Você perdeu!')
    elif jogador == 1:
        print('EMPATE!')
    elif jogador == 2:
        print('Você ganhou!')
    else:
        print('Jogada invalida')
elif computador == 2:
    if jogador == 0:
        print('Você ganhou!')
    elif jogador == 1:
        print('Você perdeu!')
    elif jogador == 2:
        print('EMPATE!')
    else:
        print('Jogada invalida')
