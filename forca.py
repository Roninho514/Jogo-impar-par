from random import randrange
def jogar():
    imprimir_abertura_jogo()
    palavra_secreta = pegando_palavras()
    letras_acertadas = criptografando_palavra(palavra_secreta)
    print(letras_acertadas)
    erros = 0
    acertou = enforcou = False
    while (not acertou and not enforcou):
        chute = receba_chute_jogador()
        if (chute in palavra_secreta):
            marca_chute_correto(palavra_secreta,chute,letras_acertadas)
        else:
            erros += 1
            desenha_forca(erros)
        print(letras_acertadas)
        enforcou = erros == 7
        acertou = '_' not in letras_acertadas
    if acertou:
        alerta_venceu()
    else:
        alerta_perdeu(palavra_secreta)
    
def imprimir_abertura_jogo():
    print("*********************************")
    print("**Bem vindo ao jogo da forca!****")
    print("*********************************")
def pegando_palavras():
    palavras = []
    arquivo = open('palavras.txt','r')
    for i in arquivo:
        i = i.strip()
        palavras.append(i)
    arquivo.close
    numero = randrange(0,len(palavras))
    palavra_secreta = palavras[numero].upper()
    return palavra_secreta

def criptografando_palavra(palavra_secreta):
    letras_acertadas = ['_' for letra in palavra_secreta]
    return letras_acertadas

def receba_chute_jogador():
    chute = str(input('Qual letra? ')).strip().upper()[0]
    return chute

def marca_chute_correto(palavra_secreta, chute,letras_acertadas):
    index = 0
    for letra in palavra_secreta:
        if (chute.upper() == letra.upper()):
            letras_acertadas[index] = chute
        index += 1

def alerta_venceu():
    print("Parabéns, você ganhou!")
    print("       ___________      ")
    print("      '._==_==_=_.'     ")
    print("      .-\\:      /-.    ")
    print("     | (|:.     |) |    ")
    print("      '-|:.     |-'     ")
    print("        \\::.    /      ")
    print("         '::. .'        ")
    print("           ) (          ")
    print("         _.' '._        ")
    print("        '-------'       ")

def alerta_perdeu(palavra_secreta):
    print("Puxa, você foi enforcado!")
    print("A palavra era {}".format(palavra_secreta))
    print("    _______________         ")
    print("   /               \       ")
    print("  /                 \      ")
    print("//                   \/\  ")
    print("\|   XXXX     XXXX   | /   ")
    print(" |   XXXX     XXXX   |/     ")
    print(" |   XXX       XXX   |      ")
    print(" |                   |      ")
    print(" \__      XXX      __/     ")
    print("   |\     XXX     /|       ")
    print("   | |           | |        ")
    print("   | I I I I I I I |        ")
    print("   |  I I I I I I  |        ")
    print("   \_             _/       ")
    print("     \_         _/         ")
    print("       \_______/           ")

def desenha_forca(erros):
    print("  _______     ")
    print(" |/      |    ")

    if(erros == 1):
        print(" |      (_)   ")
        print(" |            ")
        print(" |            ")
        print(" |            ")

    if(erros == 2):
        print(" |      (_)   ")
        print(" |      \     ")
        print(" |            ")
        print(" |            ")

    if(erros == 3):
        print(" |      (_)   ")
        print(" |      \|    ")
        print(" |            ")
        print(" |            ")

    if(erros == 4):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |            ")
        print(" |            ")

    if(erros == 5):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |            ")

    if(erros == 6):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |      /     ")

    if (erros == 7):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |      / \   ")

    print(" |            ")
    print("_|___         ")
    print()

if(__name__ == '__main__'):
    jogar()