def area(largura, comprimento):
    a = largura * comprimento
    print(f'A área de um terreno {largura}x{comprimento} é de {a}m².')


print('Controle de terrenos')
print('-' * 20)
larg = float(input('Largura (m) : '))
compri = float(input('Comprimento (m) : '))
area(larg, compri)