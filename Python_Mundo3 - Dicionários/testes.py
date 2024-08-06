# pessoas = {} #dicionários sempre são usados como chaves.
# tupla = () #tuplas sempre são usadas com parenteses.
# lista = [] #listas são declaradas com colchetes.

pessoas = {'nome': 'Daniel', 'sexo': 'M', 'idade': 22}
print(pessoas['nome'])

print(f'O {pessoas["nome"]} tem {pessoas["idade"]} anos') #quando você vai fazer uma referencia ao nome, ou idade, você precisa colocar colchetes, e usar aspas duplas.
print(f'O {pessoas["nome"]} é {pessoas["sexo"]}')
print(pessoas.keys()) #mostra as chaves do dicionário, como por exemplo o indice nome, indice sexo e indice idade
print(pessoas.values()) #mostra os valores, como por exemplo os valores Daniel, M, e 22
print(pessoas.items()) #mostra todos os itens que existem no dicionário.

print("*----*" * 15)

for chaves in pessoas.values():
    print(chaves)
print("*----*" * 15)

for chaves in pessoas.keys():
    print(chaves)

print("*----*" * 15)

for chaves, valores in pessoas.items():
    print(f'{chaves} = {valores}')

print("*----*" * 15)

pessoas = {'nome': 'Daniel', 'idade': 22, 'sexo': 'M'}
del pessoas['sexo'] #deleta algum elemento.
pessoas['nome'] = 'Aline' #troca o nome do daniel por aline
pessoas['peso'] = 72.0 #ele também adiciona itens.

print("*----*" * 15)

brasil = []
estado1 = {'uf': 'Rio de Janeiro', 'sigla': 'RJ'}
estado2 = {'uf': 'São Paulo', 'sigla': 'SP'}
brasil.append(estado1) #adicionando valores dentro da lista
brasil.append(estado2)
print(estado1)
print(estado2)
print(brasil) #criando um dicionário dentro de uma lista.

print(brasil[0] ['uf']) #mostra o Rio de Janeiro porque está no índice 0 e o uf é Rio de Janeiro.


print("*----*" * 15)


estado = {}
brasil = []

for contador in range(0, 3):
    estado['uf'] = str(input('Unidade Federativa: '))
    estado['sigla'] = str(input('Sigla do Estado: '))
    brasil.append(estado.copy()) #copy faz uma cópia do elemento quando usa dicionário.
print(brasil)

pessoas = {'nome': 'Daniel', 'sexo': 'M', 'idade': 22}
print(f'O {pessoas["nome"]} tem {pessoas["idade"]} anos')
