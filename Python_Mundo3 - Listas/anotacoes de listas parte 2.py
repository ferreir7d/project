# teste = []
# teste.append('Daniel')
# teste.append(22)
#
# galera = []
# galera.append(teste[:]) #esse [:] criou uma cópia da lista,
#
# teste [0] = 'Aline'
# teste [1] = 23
# galera.append(teste[:])
# print(galera)
#
# # ______________________________________________________________________________________________
#
# galera = [['Daniel', 22], ['Aline', 22], ['Isabelly', 10], ['Francisco', 47]]
# print(galera[3] [1]) #pega o indice 0, cada indice é um valor, daniel indice 0, 22 indice 0, aline indice 1, 22 da idade indice 1
#
# ------------------------------------------------------------------------------------------------------------
#
# galera = [['Daniel', 22], ['Aline', 22], ['Isabelly', 10], ['Francisco', 44]]
# for pessoa in galera:
#     # print(pessoa[0], end=', ')
#     print(f'{pessoa[0]} tem {pessoa[1]} anos de idade')
#
# --------------------------------------------------------------------------------------------------------------
#
# galera = []
# dados = []
# totalmaioridade = totalmenoridade = 0
#
# for contador in range(0, 3):
#     dados.append(str(input('Nome:')))
#     dados.append(int(input('Idade: ')))
#     galera.append(dados[:]) #cópia de dados.
#     dados.clear()
#
# for pessoa in galera:
#     if pessoa[1] >= 21:
#         print(f'{pessoa[0]} é maior de idade.')
#         totalmaioridade += 1
#     else:
#         print(f'{pessoa[0]} é menor de idade.')
#         totalmenoridade += 1
# print(f'Temos {totalmaioridade} maiores de idade e {totalmenoridade} menores de idade')
