from datetime import date

atual = date.today().year

soma_de_idades = 0
media_das_idades = 0
maioridadehomem = 0
nomevelho = ''
total_idade_mulher_20 = 0

for pessoa in range(1, 5):
    print("º{} PESSOA ".format(pessoa))
    nome = str(input("Nome: ")).strip()
    idade = int(input("Idade: "))
    sexo = str(input("Sexo [M/F] ")).strip()
    soma_de_idades += idade

    if pessoa == 1 and sexo in "Mm":
        maioridadehomem = idade
        nomevelho = nome
    if sexo in "Mm" and idade > maioridadehomem:
        maioridadehomem = idade
        nomevelho = nome
    if sexo in 'Ff' and idade < 20:
        total_idade_mulher_20 += total_idade_mulher_20 + 1
media_das_idades = soma_de_idades / 4

print("A média das idades é de {} anos. ".format(media_das_idades))
print("O homem mais velho tem {} anos e se chama {} ".format(maioridadehomem, nomevelho))
print("Ao todo tem {} mulher com menos de 20 anos. ".format(total_idade_mulher_20))



