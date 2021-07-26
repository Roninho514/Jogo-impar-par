from datetime import date
anoAtual = date.today().year
sexo = str(input('Qual o seu sexo? (M)masculino (F)feminino\n')).upper()
if sexo == 'F':
    print('Você não precisa fazer o alistamento')
elif sexo == 'M':
    anoNasc = int(input('Em que ano você nasceu?\n'))
    idade = anoAtual - anoNasc
    if idade == 18:
        print('Você tem {} anos se aliste IMEDIATAMENTE'.format(idade))
    elif idade > 18:
        anosDeveria = idade - 18
        anoAlistamento = anoAtual-anosDeveria
        print('Você tem {} anos deveria ter se alistado em {}'.format(idade, anoAlistamento))
    else:
        anosFaltam = 18 - idade
        print('Você tem {} anos ainda faltam {} anos para se alistar'.format(idade, anosFaltam))
else:
    print('Você deve ter digitado alguma tecla errada')