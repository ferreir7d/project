totalmulheres = 0
totalhomens = 0
total18 = 0
while True:
    idade = int(input('Idade: '))
    sexo = ' '
    while sexo not in "MF":
        sexo = str(input("Digite o sexo: [M/F] ")).strip().upper()[0]

    if idade >= 18:
        total18 += 1

    if sexo == "F":
        totalmulheres += 1
    elif sexo == "M":
        totalhomens += 1
    resposta = ' '
    while resposta not in "SN":
        resposta = str(input("Quer continuar? [S/N] ")).strip().upper()[0]
    if resposta == "N":
        break
    print(f'A idade é {idade} e o sexo é {sexo} ')
print(f"Total de pessoas com mais de 18 anos {total18}")
print(f'Total de homens {totalhomens}')
print(f'Total de mulheres {totalmulheres}')

