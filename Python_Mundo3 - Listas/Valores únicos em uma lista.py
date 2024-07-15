
valores = []
while True:
    numero = (int(input('Digite um número: ')))
    if numero not in valores:
        valores.append(numero)
    else:
        print('Valor duplicado, não vou adicionar')
    resposta = ' '
    while resposta not in "SN":
        resposta = str(input('Quer continuar? ')).strip().upper()[0]
    if resposta == 'N':
        break
    valores.sort()
print(f'Os valores em ordem são: {valores}')
