# numero = soma = 0
# while True:
#     numero = int(input("Digite um número: "))
#     if numero == 999:
#         break
#     soma = soma + numero
# print("A soma vale {}".format(soma))
# print(f"A soma vale {soma}") #interpolação de string, jeito melhor e mais fácil de fazer.




numero = soma = 0
while True:
    numero = int(input("Digite um número: "))
    if numero == 999:
        break
    soma += numero
print(f'A soma vale {soma}')

#1