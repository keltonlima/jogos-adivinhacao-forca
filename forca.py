import random
import mensagens_do_jogo

def jogar():
    
    mensagem_de_abertura()
    
    palavra_secreta = carrega_palavra_secreta()
    
    letras_acertadas = mostra_letras_acertadas(palavra_secreta)
    
    print(letras_acertadas)
    
    acertou = False
    enforcou = False
    tentativas = 0
    rodada = 1

    while not acertou and not enforcou:
        
        print("Rodada {}\n".format(rodada)) # mostrar quantidade máxima de tentativas
        
        chute = pede_chute()
        
        if chute in palavra_secreta:
            marca_chute_jogador(chute, palavra_secreta, letras_acertadas)
        
        else:
            tentativas += 1
        
        enforcou = tentativas == 7
        
        acertou = "_" not in letras_acertadas
        print(letras_acertadas)
        
        rodada += 1

    if acertou:
        mensagens_do_jogo.imprime_mensagem_vencedor()
        
    else:
        mensagens_do_jogo.imprime_mensagem_perdedor(palavra_secreta)

def mensagem_de_abertura():
    print("**************************")
    print("Bem vindo ao jogo da Forca")
    print("**************************")

def carrega_palavra_secreta():
    arquivo = open("palavras.txt", "r")
    palavras = []
    
    with open("palavras.txt", "r") as arquivo:
        for linha in arquivo:
            linha = linha.strip()
            palavras.append(linha)
    
    numero = random.randrange(0, len(palavras))

    palavra_secreta = palavras[numero].upper()
    
    return palavra_secreta

def mostra_letras_acertadas(palavra):
    return ["_" for letra in palavra]

def pede_chute():
    chute = input("Qual letra?\n")
    chute = chute.strip().upper()
    return chute
    
def marca_chute_jogador(chute, palavra_secreta, letras_acertadas):
    index = 0
    for letra in palavra_secreta:
        if chute == letra:
            letras_acertadas[index] = letra
        index += 1
            
if __name__ == "__main__":
    jogar()