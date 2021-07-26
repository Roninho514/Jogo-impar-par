sexo = str(input('Digite o seu sexo [M/F]: ')).upper().strip()[0]
while sexo not in 'MF':
    print('Você digitou algo errado tente novamente')
    sexo = str(input('Digite o seu sexo [M/F]: ')).upper().strip()
print('Seu sexo é {}'.format(sexo))