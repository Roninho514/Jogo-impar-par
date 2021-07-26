while True:
    valor = int(input('Qual valor você quer saber a tabuada? '))
    if valor >= 0:
        print(10*'=-=')  
        for i in range(1,11):
            print(f'{valor} x {i} = {valor * i}')
        print(10*'=-=')
    else:
        break
print('Obrigado por acessar')