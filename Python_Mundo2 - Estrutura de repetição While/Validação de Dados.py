sexos = "F" and "M"
while sexos == "F" or "M":
    sexo = str(input("Digite o seu sexo:")).upper()
    if sexos != sexo:
        print("Digite o seu sexo corretamente!")
    else:
        print("Obrigado")
print("fim")

