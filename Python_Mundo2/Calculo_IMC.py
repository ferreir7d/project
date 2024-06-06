peso = float(input("Digite o seu peso: (Kg) "))
altura = float(input("Digite a sua altura: (m) "))

imc = peso / (altura ** 2)
print("O imc dessa pessoa é de {:.1f}".format(imc))

if imc < 18.5:
    print("Você está abaixo do peso")
elif imc >= 18.5 or imc < 25:
    print("Peso Ideal")
elif imc == 25 or imc < 30:
    print("Sobrepeso")
elif imc >= 30 or imc < 40:
    print("Obesidade")
else:
    print("Obesidade Mórbita")
