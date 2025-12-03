
from random import randint
from time import sleep
print("-=" * 20)
print(" Jogo do PAR ou ÍMPAR ".center(40))
print("-=" * 20)

vitorias = 0
while True:
    jogador = int(input("Escolha um número: "))
    computador = randint(0, 10)
    total = jogador + computador

    #Entrada de escolha do jogador:
    escolha = " "
    while escolha not in "PI":
         escolha = str(input("Par ou ímpar ? [P/I] ")).strip().upper()[0]
         if escolha not in "PI":
             print("> Letra inválida! Tente P ou I.")
    print("-=" * 20)

    print(f"Você jogou {jogador} e o computador jogou {computador}. Total de {total}.")

    #Verificar se deu par ou ímpar:
    if total % 2 == 0:
        resultado = "P"
        print("> Deu PAR!")

    else:
        resultado = "I"
        print("> Deu ÍMPAR!")

    #Checar a vitoria:
    if escolha == resultado:
        print("Você VENCEU!!! :D")
        vitorias += 1
        print("> Vamos jogar novamente ?")
        print("-=" * 20)
        sleep(1.5)

    else:
        print("Você PERDEU! :(")
        print("-=" * 20)
        break

sleep(1)
print(f"GAME OVER! Você venceu {vitorias} vez(es).")








