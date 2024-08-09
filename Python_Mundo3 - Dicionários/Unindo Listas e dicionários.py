pessoas = {} #dicionário
galera = [] #lista
soma = media = 0

while True:

    pessoas['nome'] = str(input('Digite o nome: '))
    pessoas['sexo'] = str(input('Digite o sexo: [M/F] ')).strip().upper()[0]
    pessoas['idade'] = int(input('Digite a idade: '))
    soma += pessoas['idade']
    galera.append(pessoas.copy())
    resposta = ' '
    while resposta not in 'SN':
        resposta = str(input('Quer continuar?')).strip().upper()[0]
    if resposta == 'N':
        break

print(pessoas)
print(f'Ao todo foram cadastradas {len(galera)} pessoas')
media = soma / len(galera)

print(f'A média das idades foram de {media} anos')
print('As mulheres cadastradas foram: ')

for p in galera:
    if p['sexo'] == 'F':
        print(f'{p["nome"]}')
