soma = 0
cont = 0
for c in range(0, 7):
    num = int(input("Digite o {}º valor: ".format(c)))
    if num % 2 == 0: #verifica se o número é divisivel por 2
        soma += num # facilitei esse, soma ele mesmo. antes ficaria assim: soma = soma + num
        cont += 1
print("Você informou {} números e a soma é {} ".format(cont, soma))

