#Recebendo os dados
numeroInteiro = int(input('Digite um número inteiro: '))
print('Você deseja converter para(digite o número):')
escolha = int(input('1 - Binário\n2 - Octal\n3 - Hexadecimal\n4 - Cancelar\n'))
#Possibilidade e cálculos
if escolha == 1:
    print('O número {} em binário ficará {}'.format(numeroInteiro,bin(numeroInteiro)[2:]))
elif escolha == 2:
    print('O número {} convertido para octal ficará {}'.format(numeroInteiro,oct(numeroInteiro)[2:]))
elif escolha == 3:
    print('O número {} convertido para hexadecimal ficará {}'.format(numeroInteiro, hex(numeroInteiro)[:2]))
elif escolha == 4:
    print('fim do programa...')
else:
    print('Essa tecla não é uma escolha, renicie o programa e tente novamente.')
