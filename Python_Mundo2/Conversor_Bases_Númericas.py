num = int(input("Digite um número inteiro: "))
print('''Escolha uma das bases para fazer a conversão:
[1] converter para BINÁRIO
[2] converter para OCTAL
[3] converter para HEXADECIMAL''')

opcao = int(input("Sua opção: "))
if opcao == 1:
    print("{} convertido para BINÁRIO é igual à {}".format(num, bin(num)))
elif opcao == 2:
    print("{} convertido para OCTAL é igual à {}".format(num, oct(num)))
elif opcao == 3:
    print("{} convertido para HEXADECIMAL é igual à {}".format(num, hex(num)))
else:
    print("opcão inválida, tente novamente!")

