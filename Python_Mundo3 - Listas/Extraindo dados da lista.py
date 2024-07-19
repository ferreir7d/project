valores = []

while True:
    valores.append(int(input('Digite um número: ')))
    resposta = ' '
    while resposta not in 'SN':
        resposta = str(input('Quer continuar? [S/N]')).strip().upper()[0]
    if resposta == 'N':
        break
    valores.sort(reverse=True) #coloca em ordem decrescente

print(f'Foram digitados {len(valores)} números') #len serve para contar quantos valores tem
print(f'Os valores em ordem decrescente são: {valores}')
if 5 in valores:
    print(f'O valor 5 foi digitado {valores.count(5)} vez e está na lista')
else:
    print(f'O valor 5 não foi encontrado.')



