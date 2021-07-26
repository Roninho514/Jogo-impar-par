SomaIdade = 0
MaisVelho = 0
ContMulher = 0
for c in range(1,5):
    print(5*'-' + ' {}ª PESSOA' .format(c) + 5*'-')
    Nome = str(input('Nome: '))
    Idade = int(input('Idade: '))
    Sexo = str(input('Sexo [M/F]: ')).upper().strip()
    print(Sexo)
    SomaIdade += Idade
    if Sexo == 'M':
        if MaisVelho < Idade:
            MaisVelho = Idade
            NomeVelho = Nome
    if Sexo == 'F' and Idade < 20:
        ContMulher +=  1
print('A média de idade do grupo é {} '.format(SomaIdade/4))
print('O homem mais velho tem {} anos e se chama {}'.format(MaisVelho, NomeVelho))
print('Ao todo são {} mulheres com menos de 20 anos'.format(ContMulher))
