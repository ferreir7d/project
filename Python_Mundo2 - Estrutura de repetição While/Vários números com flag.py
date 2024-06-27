leitura_numeros = 0
soma = 0


while True:
    numeros = int(input("Digite um número: "))

    if numeros == 999:
        break
    elif numeros > 0:
        leitura_numeros = leitura_numeros + 1
    soma = soma + numeros

print(f"A soma vale {soma}")
print(f"Foram digitados {leitura_numeros} números")