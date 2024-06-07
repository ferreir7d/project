from random import randint  #Gerar um número inteiro aleatório entre 1 e 10
from time import sleep
itens = ("Pedra", "Papel", "Tesoura")
computador = randint(0, 2)

print('''Escolha uma opção: 
[0] PEDRA
[1] PAPEL
[2] TESOURA ''')

jogador = int(input("Pedra, papel ou tesoura? "))
print("JO")
sleep(1)
print("KEM")
sleep(1)
print("PO")
sleep(1)

print("------------" * 10)
print("O computador escolheu: {}".format(itens[computador])) #entre colchetes para indicar a posição
print("O jogador escolheu: {}".format(itens[jogador]))
print("------------" * 10)
if computador == 0: #Computador escolheu PEDRA
    if jogador == 0:
        print("Vocês empataram!!!")
    elif jogador == 1:
        print("O jogador venceu!!!")
    elif jogador == 2:
        print("O computador venceu!!!")
    else:
        print("Jogada Inválida, tente novamente!!!")
elif computador == 1: #Computador escolheu PAPEL
    if jogador == 0:
        print("O computador venceu!!!")
    elif jogador == 1:
        print("Vocês empataram!!!")
    elif jogador == 2:
        print("O jogador venceu!!!")
    else:
        print("Jogada Inválida, tente novamente!!!")
elif computador == 2: #Computador escolheu TESOURA
    if jogador == 0:
        print("O jogador Venceu!!!")
    elif jogador == 1:
        print("O computador venceu!!!")
    elif jogador == 2:
        print("Vocês empataram!!!")
    else:
        print("Jogada Inválida, tente novamente!!!")
