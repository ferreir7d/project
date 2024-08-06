from datetime import datetime

dados = {}

dados['nome'] = str(input('Nome: '))
nasc = int(input('Ano de nascimento: '))
dados['idade'] = datetime.now().year - nasc
dados['CTPS'] = int(input('Carteira de trabalho: '))

if dados['CTPS'] != 0:
    dados['contratação'] = int(input('Ano de contratação: '))
    dados['salário'] = float(input('Salário: R$'))
    dados['aposentadoria'] = dados['idade'] + ((dados['contratação'] + 35) - datetime.now().year)

print(dados)

for chave, valor in dados.items():
    print(f'{chave} tem o valor {valor}')
    