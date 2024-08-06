# aluno = {} #dicionário
#
# aluno['nome'] = str(input('Digite o nome: '))
# aluno['media'] = float(input(f'A média de {aluno["nome"]}: '))
# if aluno['media'] >= 7:
#     aluno['situação'] = 'Aprovado'
# elif 5 <= aluno['media'] < 7:
#     aluno['situação'] = 'Reprovado'
# else:
#     aluno['situação'] = 'Reprovado'
#
# print(aluno)



#2 FORMAS DE FAZER


entrada1 = str(input('Digite o seu nome: '))
entrada2 = float(input('Digite a sua média: '))

if entrada2 <= 5:
    situacao = 'Reprovado.'
elif entrada2 <= 6.9:
    situacao = 'Recuperação.'
else:
    situacao = 'Aprovado!'

dados = {'Nome': entrada1, 'Média': entrada2, 'Situação': situacao}
print(f'Nome do Aluno: {dados["Nome"]}')
print(f'Média do Aluno: {dados["Média"]}')
print(f'Situação do Aluno: {dados["Situação"]}')
