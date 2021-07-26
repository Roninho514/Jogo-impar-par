termo = int(input('Digite o primeiro termo: '))
razao = int(input('Digite a razão: '))
termoMais = 1
c = 1
quantTermo = 10
while termoMais != 0:
    while  c < 11:
        an = termo + (c-1)*razao
        print(an , '-> ' if c < 10 else '', end='')
        c += 1
    print('pausa')
    termoMais = int(input('Quantos termos você ainda quer mostrar mais?\n'))
    quantTermo += termoMais
    contadorTermosMais = 1
    while contadorTermosMais < termoMais + 1:
        an = termo + (c-1)*razao
        print(an , '-> ' if contadorTermosMais < termoMais else '', end='')
        c += 1
        contadorTermosMais += 1
print('Progressão finalizada com {} termos'.format(quantTermo))