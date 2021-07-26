def jogar():
    print("*********************************")
    print("**Bem vindo ao jogo da forca!****")
    print("*********************************")
    palavra_secreta = 'banana'
    acertou = enforcou = False
    while (not acertou and not enforcou):
        chute = str(input('Qual letra? ')).strip()[0]
        index = 0
        for letra in palavra_secreta:
            if (chute == letra ):
                print(f'Encontrei a letra {chute} na posição {index}')
            index += 1
        print('Jogando...')
if(__name__ == '__main__'):
    jogar()