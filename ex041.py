from datetime import date
anoAtual = date.today().year
anoNasc = int(input('Digite o seu ano de nascimento: '))
idade = anoAtual - anoNasc
if idade <= 9:
    print('Você tem {} anos e está na categoria mirim.'.format(idade))
elif idade > 9 and idade <= 14:
    print('Você tem {} anos e está na categoria infantil.'.format(idade))
elif  idade > 14 and idade <= 19:
    print('Você tem {} anos e está na categoria júnior.'.format(idade))
elif idade > 19 and idade <= 25:
    print('Você tem {} anos e está na categoria sênior.'.format(idade))
else:
    print('Você tem {} anos e está na categoria master.'.format(idade))
