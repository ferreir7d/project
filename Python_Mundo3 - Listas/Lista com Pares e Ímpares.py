numeros = [[], []] #posição 0 e posição 1
valores = 0

for posicao in range(1, 8):
    valores = int(input(f'Digite o {posicao} valor: '))
    if valores % 2 == 0:
        numeros[0].append(valores)
    else:
        numeros[1].append(valores)
numeros[0].sort() #colocando os números em ordem
numeros[1].sort()
print(f'Os valores pares foram: {numeros[0]}') #colocando a primeira posicao da chave de números, que é 0
print(f'Os valores ímpares foram: {numeros[1]}')
