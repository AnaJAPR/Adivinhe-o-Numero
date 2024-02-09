import random
from time import sleep

# Desenvolver uma interface em que o usuário tenta adivinhar um número de 1 a 100 gerado aleatoriamente

nome_do_jogador = input("Olá, qual é o seu nome?  ")
sleep(2)
print(f"Bem-vindo(a) {nome_do_jogador}!")
sleep(1)
print("Gostaria de jogar Adivinhe o Número? ")
sleep(1)
print("0.Não \n1.Sim")
sleep(1)
jogar = True
while jogar == True:
    try:
        escolha_de_jogar = int(input("Sua resposta: "))
        if escolha_de_jogar == 0:
            print(f"Ok, {nome_do_jogador}. Até logo! ")
            jogar = False
            break

        elif escolha_de_jogar == 1:
            print(f"Vamos jogar então {nome_do_jogador}!")
            sleep(1)
            print("Você tem 10 chances de acertar o número sorteado de 1 a 100!")
            sleep(2)
            num_sorteado = random.randint(1,100)
            quant_chutes = 0
            while quant_chutes < 10:
                num_chutado = int(input("Qual é o seu chute? "))
                quant_chutes += 1
                if num_chutado > num_sorteado:
                    print("Chute mais baixo!")
                elif num_chutado < num_sorteado:
                    print("Chute mais alto!")
                else:
                    print("Parabéns, você acertou o número!")
                    quant_chutes = 10
                    sleep(1)
                    print("Gostaria de continuar o jogo?")
                    sleep(1)
                    print("0.Não \n1.Sim")
                    sleep(1)
                    jogar = True
        else:
            print("Resposta inválida, digite 0 ou 1")
            jogar = False
            break
         
    except:
        print("Resposta inválida, vamos começar novamente...")
        sleep(2)
        print("Gostaria de jogar Adivinhe o Número? ")
        sleep(1)
        print("0.Não \n1.Sim")
        sleep(1)
        jogar = True
        

    
    
    
    
    
    
    
# adicionar pontuação a cada acerto
# exceção pra caso o chute não esteja entre 0 e 100
# exceção para nome do jogador não ser qualquer coisa