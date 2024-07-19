listatemporaria = []
pessoaslistaprincipal = []
maispesadas = maisleves = 0

while True:
    listatemporaria.append(str(input('Nome: ')))
    listatemporaria.append(float(input('Peso: ')))

    pessoaslistaprincipal.append(listatemporaria[:])  #ele está criando uma cópia da lista temporaria para a principal

    if len(pessoaslistaprincipal) == 1:
        maispesadas = maisleves = listatemporaria[1]
    else:
        if listatemporaria[1] > maispesadas:
            maispesadas = listatemporaria[1]
        if listatemporaria[1] < maisleves:
            maisleves = listatemporaria[1]

    resposta = ' '
    while resposta not in 'SN':
        resposta = str(input('Quer continuar? [S/N]')).strip().upper()[0]
    if resposta == 'N':
        break

    listatemporaria.clear()  # ele limpa a lista temporaria e deixa só a principal
print(f'Os dados foram {pessoaslistaprincipal}')
print(f'Ao todo, foram cadastradas {len(pessoaslistaprincipal)} pessoas.')
print(f'O maior peso foi de {maispesadas}')
print(f'O menor peso foi de {maisleves}')
