import forca
import adivinhacao

def escolher_jogo():
    print("***************************")
    print("Escolha o que deseja jogar.")
    print("***************************")

    escolha_do_jogo = int(input("1 - Jogo de Adivinhação\n2 - Jogo da Forca\n"))

    if escolha_do_jogo == 1:
        adivinhacao.jogar()
    else:
        forca.jogar()

if __name__ == "__main__":
    escolher_jogo()