from datetime import date #importar o ano atual

atual = date.today().year #verifica o ano de hoje

nascimento = int(input("Digite o ano que você nasceu: "))
idade = atual - nascimento
sexo = str(input("Digite o seu sexo: "))

print("O seu sexo é {}.".format(sexo))

if sexo == "masculino":
    print("Você é homem, deverá se alistar.")
else:
    print("Você é mulher, não precisará de alistamento.")

print("Quem nasceu em {} tem {} anos em {}.".format(nascimento, idade, atual))

if idade == 18:
    print("Chegou a hora de você se alistar")
elif idade > 18:
    saldo = idade - 18
    print("Já passou da hora de você se alistar. Você deveria ter se alistado há {} anos!".format(saldo))
    ano = atual - saldo
    print("Seu alistamento foi em {}".format(ano))
elif idade < 18:
    saldo = idade - 18
    print("Você ainda não tem 18 anos. Faltam ainda {} anos para você se alistar".format(saldo))
    ano = atual + saldo
    print("Seu alistamento será em {}".format(ano))
