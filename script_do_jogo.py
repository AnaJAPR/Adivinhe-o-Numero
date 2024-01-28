import random
from time import sleep
    
# tentando desenvolver o script apenas com testes, sem consultar a internet
nome_do_jogador = input("Olá, qual é o seu nome?  ")
sleep(1)
print(f"Bem-vindo(a) {nome_do_jogador}!")
sleep(1)
escolha_de_jogar = int(input("Gostaria de jogar Adivinhe o Número? "))
if escolha_de_jogar == 0:
    print(f"Ok, {nome_do_jogador}. Até logo! ")
elif escolha_de_jogar == 1:
    num_sorteado = random.randint(1,100)
    print(f"Vamos começar o jogo então {nome_do_jogador}!")
    sleep(1)
    print("Você tem 5 chances de acertar o número sorteado de 1 a 100")
    sleep(2)
    num_chutado = int(input("Qual é o seu chute? "))
    quant_chutes = 0
    # if num_chutado > num_sorteado:
    #     print("Chute mais baixo!")
    # elif num_chutado < num_sorteado:
    #     print("Chute mais alto!")
    # else:
    #     print("Parabéns você acertou o número!")
    while quant_chutes <= 5 and num_chutado != num_sorteado:
        quant_chutes += 1
        num_chutado

else:
    print("Resposta inválida, digite 0 ou 1")
    