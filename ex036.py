valorCasa = float(input('Qual o valor da sua casa?\n'))
salario = float(input('Qual o seu salário por mês?\n'))
anosPagamento = int(input('Em quantos anos vai pagar?\n'))
prestacaoMensal = valorCasa/(anosPagamento*12)
if prestacaoMensal > (salario*30)/100:
    print('Empréstimo negado')
else:
    print('Empréstimo feito, você deverá pagar {:.2f} por mês'.format(prestacaoMensal))
