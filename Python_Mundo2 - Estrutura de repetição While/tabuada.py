while True: #loop infinito
    numero = int(input("Quer verificar a tabuada de qual valor? "))
    if numero < 0:
        break
    print("*****" * 10)
    for contador in range(1, 11):
        print(f' {numero} x {contador} = {numero * contador}')

    print("****" * 10)


numero = int(input("Digite um número: "))
for c in range(1, 11):
    if numero < 0:
        break
    print(f' {numero} x {c} = {numero*c}')
