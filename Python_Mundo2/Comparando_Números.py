num = int(input("Digite um número: "))
num2 = int(input("Digite outro número: "))

if num > num2:
    print("O primeiro valor {} é maior do que o segundo valor {} ".format(num, num2))
elif num == num2:
    print("O primeiro valor {} é igual ao segundo valor {}".format(num, num2))
elif num2 > num:
    print("O segundo valor {} é maior do que o primeiro valor {}".format(num2, num))
