from datetime import date
AnoAtual = date.today().year
MaiorIdade = 0
MenorIdade = 0
for c in range(1,8):
    pessoa = int(input('Digite o ano que a {}ª pessoa nasceu:'.format(c)))
    if  AnoAtual - pessoa >= 18:
        MaiorIdade += 1
    else:
        MenorIdade += 1
print('Ao todo tivemos {} pessoas maiores de idade'.format(MaiorIdade))
print('Ao todo tivemos {} pessoas menores de idade'.format(MenorIdade))