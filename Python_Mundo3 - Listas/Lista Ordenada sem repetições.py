# valores = []
#
# for valor in range(0, 5):
#     numero = int(input('Digite um valor: '))
#     if valor == 0: #se valor for o primeiro
#         valores.append(numero)
#     elif numero > valores[-1]: #se o número for maior do que o último elemento
#         valores.append(numero)
#     else:
#         posicao = 0
#         while posicao < len(valores):
#             if numero <= valores[posicao]:
#                 valores.insert(posicao, numero)
#                 break
#             posicao += 1
# print(f'Os valores digitados em ordem são {valores}')
#
# # Daria para simplificar usando o sort que ordena, mas o guanabara quis utilizar sem.

valores = []

for valor in range(0, 5):
    valores.append(int(input('Digite um número: ')))
    valores.sort()
print(f'Os valores em ordem são: {valores}')

# do jeito com o sort.