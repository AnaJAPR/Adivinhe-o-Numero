import random
from time import sleep

# Desenvolver uma interface em que o usuário tenta adivinhar um número de 1 a 100 gerado aleatoriamente

nome_do_jogador = input("Olá, qual é o seu nome?  ")
sleep(1)
print(f"Bem-vindo(a) {nome_do_jogador}!")
sleep(1)
print("Gostaria de jogar Adivinhe o Número? ")
sleep(1)
print("0.Não \n1.Sim")
escolha_de_jogar = int(input("Sua resposta: "))


if escolha_de_jogar == 0:
    print(f"Ok, {nome_do_jogador}. Até logo! ")
    
elif escolha_de_jogar == 1:
    print(f"Vamos começar o jogo então {nome_do_jogador}!")
    sleep(1)
    print("Você tem 10 chances de acertar o número sorteado de 1 a 100")
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
            print("Parabéns você acertou o número!")
            break
else:
    print("Resposta inválida, digite 0 ou 1")
    