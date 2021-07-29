def jogar():
    print("*********************************")
    print("**Bem vindo ao jogo da forca!****")
    print("*********************************")
    palavra_secreta = 'Uva'.upper()
    letras_acertadas = ['_' for letra in palavra_secreta]
    print(letras_acertadas)
    erros = 0
    acertou = enforcou = False
    while (not acertou and not enforcou):
        chute = str(input('Qual letra? ')).strip().upper()[0]
        if (chute in palavra_secreta):
            index = 0
            for letra in palavra_secreta:
                if (chute.upper() == letra.upper() ):
                    letras_acertadas[index] = chute
                index += 1
        else:
            erros += 1
        print(letras_acertadas)
        enforcou = erros == 6
        acertou = '_' not in letras_acertadas
    if acertou:
        print('Parabéns você foi o vencedor')
    else:
        print('Você perdeu')
if(__name__ == '__main__'):
    jogar()