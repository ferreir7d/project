total = totalmaisdemil = menor = contador = 0
barato = ''
while True:
    produto = str(input("Digite o nome do produto: "))
    preco = float(input('Digite o preço do produto: R$'))
    total += preco
    if preco > 1000:
        totalmaisdemil += 1
    if contador == 1 or preco < menor:
        menor = preco
        barato = produto
    resposta = ' '
    while resposta not in "SN":
        resposta = str(input("Quer continuar? [S/N]")).strip().upper()[0]
    if resposta == "N":
        break

print(f'O total da compra foi R${total:.2f}')
print(f'Temos {totalmaisdemil} produtos custando mais de R$1000,00')
print(f'O produto mais barato foi {barato} que custa {menor:.2f}')
