from random import randint
print(10*'#=#')
print('Bem vindo ao jogo de advinhação!')
print(10*'#=#')
vidas = 5
numeroSecreto = randint(0,100)
while vidas > 0:
    chute = int(input('Digite um numero: '))
    print(f'Você digitou o número {chute}')
    if vidas > 0 and chute == numeroSecreto:
        print('Você acertou!!')
        break
    elif vidas > 0 and chute > numeroSecreto or chute < numeroSecreto:
        if numeroSecreto > chute:
            print('Mais...')
            vidas -= 1
        else:
            print('Menos')
            vidas -= 1
if vidas == 0:
    print(f'Você perdeu!! era o número {numeroSecreto}')
print('Fim do programa!')
