import forca
import adivinhacao
print(14*"*")
print("Bem vindo a minha biblioteca de jogos!")
print(14*"*")
print("""----Escolha o jogo---- 
         (1) Forca (2) Advinhação""")
escolha_jogo = int(input("Escolha: "))
if (escolha_jogo == 1):
    forca.jogar()
elif(escolha_jogo == 2):
    adivinhacao.jogar()