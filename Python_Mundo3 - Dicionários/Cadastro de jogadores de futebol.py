dados = {}
gols = []
dados['nome'] = str(input('Nome do jogador: '))
dados['partidas'] = int(input(f'Quantas partidas jogou {dados["nome"]}: '))

for contador in range(1, dados['partidas']):
    gols.append(int(input(f'Quantos gols {dados["nome"]} fez na partida {contador}?')))

print(f'Nome do jogador: {dados["nome"]}')
print(f'Partidas: {dados["partidas"]}')
print("Gols: ")
print(gols)


print(dados)


