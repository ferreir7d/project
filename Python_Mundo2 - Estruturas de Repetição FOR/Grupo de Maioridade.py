from datetime import date

atual = date.today().year


total_de_maioridade = 0
total_de_menor = 0
for pessoa in range(1, 8):
    nascimento = int(input("Em que ano a {}º pessoa nasceu? ".format(pessoa)))
    idade = atual - nascimento

    if idade >= 18:
        total_de_maioridade = total_de_maioridade + 1
    else:
        total_de_menor = total_de_menor + 1
print("Tem {} pessoas que atigiram a maioridade e {} que não atingiram a maioridade ".format(total_de_maioridade, total_de_menor))

