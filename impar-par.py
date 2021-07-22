from random import randint
partidas = 0
while True:
    print(10*'=-')
    print('Vamos jogar par ou impar?')
    print(10*'=-')
    numeroComputador = int(randint(0,10))
    numeroJogador = int(input('Digite um valor: '))
    print('''
        [P] Par
        [I] Impar''')
    jogadorEscolha = str(input('Escloha: ')).strip().upper()[0]
    if jogadorEscolha == 'P':
        computadorEscolha = 'I'
    else:
        computadorEscolha = 'P'
    total = numeroComputador + numeroJogador
    if total%2 == 0:
        if computadorEscolha == 'P':
            vencedor = 'Computador'
        elif jogadorEscolha == 'P':
            vencedor = 'Você'
    else:
        if computadorEscolha == 'I':
            vencedor = 'Computador'
        elif jogadorEscolha == 'I':
            vencedor = 'Você'
    print(f'O computador escolheu o número {numeroComputador}')
    print(f'Total {total} o vencedor foi {vencedor}')
    if vencedor == 'Computador':
        break
    else:
        partidas += 1
print(f'GAME OVER !!!  Você ganhou {partidas} partidas')
