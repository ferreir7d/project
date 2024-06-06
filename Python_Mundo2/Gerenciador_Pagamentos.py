preco = float(input("Qual foi o preço das compras? R$"))
print('''ESCOLHA UMA FORMA DE PAGAMENTO:
[1] PIX | DINHEIRO
[2] 1X NO CŔEDITO
[3] 2X NO CRÉDITO
[4] 3X OU MAIS NO CRÉDITO ''')

opcao = int(input("Qual é a forma de pagamento?"))

if opcao == 1:
    total = preco - (preco * 10 / 100)

elif opcao == 2:
    total = preco - (preco * 5 / 100)
elif opcao == 3:
    total = preco
    parcela = total / 2
    print("Sua compra foi parcelada em 2x de R${:.2f}".format(parcela))
elif opcao == 4:
    total = preco + (preco * 20 / 100)
    total_parcelas = int(input("Quantas parcelas? "))
    parcela = total / total_parcelas
    print("Sua compra será {}x no crédito de R$ {:.2f} com JUROS.".format(total_parcelas, parcela))
else:
    total = preco
    print("OPÇÃO INVÁLIDA")

print("Sua compra de R$ {:.2f} vai custar R$ {:.2f} reais com desconto.".format(preco, total))