num = int(input('Digite um número:'))
u = num // 1 % 10
d = num // 10 % 10
c = num // 100 % 10
m = num // 1000 % 10
print('Analisando o número {}'.format(num))
print('A quantidade de unidade é {} \n a de dezena é {}'.format(u,d))
print('de centena é {} \n a de milhar é {}'.format(c,m))