import random
import mensagens_do_jogo

def jogar():
    
    mensagem_de_abertura()
    
    numero_secreto = random.randrange(1, 101)
    total_de_tentativas = 0
    rodada = 1
    pontos = 1000

    total_de_tentativas = nivel_do_jogo()

    while rodada <= total_de_tentativas:
        print("Rodada {} de {} \n".format(rodada, total_de_tentativas))
        
        numero = pega_chute()
        
        if numero < 1 or numero > 100:
            print("Tá cego? \nDigite um valor entre 1 e 100. ")
            continue

        usuario_acertou = numero_secreto == numero

        input_maior = numero_secreto < numero

        input_menor = numero_secreto > numero

        if usuario_acertou:
            print("Acertô mizerave!")
            mensagens_do_jogo.imprime_mensagem_vencedor()
            break
        else:
            print("Errrrooouuuu!")
            if input_maior:
                print("Você digitou um número maior que o número secreto\n")
            elif input_menor:
                print("Você digitou um número menor que o número secreto\n")

            pontos_perdidos = abs(pontos - numero_secreto)
            pontos = pontos_perdidos

        rodada += 1
            
    print("Fim do Jogo! Você fez {} ".format(pontos),"pontos.")
    print("O número secreto é {} ".format(int(numero_secreto)))

def mensagem_de_abertura():
    print("********************************")
    print("Bem vindo ao jogo de adivinhação")
    print("********************************")
    
def nivel_do_jogo():
    print("Deseja jogar em qual nível?\n")
    nivel_do_jogo =  int(input("1 = Básico \n2 = Intermediário \n3 = Avançado\n"))
    if nivel_do_jogo == 1:
        total_de_tentativas = 20
    elif nivel_do_jogo == 2:
        total_de_tentativas = 10
    elif nivel_do_jogo == 3:
        total_de_tentativas = 5
    return total_de_tentativas

def pega_chute():
    chute_do_usuario = input("Digite o valor do número secreto entre 1 e 100. \n")
    numero = int(chute_do_usuario)
    return numero

if __name__ == "__main__":
    jogar()