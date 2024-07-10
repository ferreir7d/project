lanche = 'Hambúrguer', 'Suco', 'Pizza', 'Pudim' #tupla
print(lanche[1:3])


#tuplas são imutáveis
lanche2 = 'Pizza', 'Água', 'Pão', 'Suco', 'Cachorro'
print(lanche2[2:])



itens = 'Carro', 'Casa', 'Iphone'
for sonhos in itens:
    print(f'Eu vou ter {sonhos}')
print('Sou foda')
print(len(itens)) #conta quantos tem

itens2 = 'Moto', 'Tenis', 'Barco'
for posicao, sonhos2 in enumerate(itens2):
    print(f'Vou ter {sonhos2} em {posicao}')


familia = 'Francisco', 'Cida', 'Isabelly', 'Aline', 'Marlene'
print(sorted(familia)) #ordena a tupla

a = 2,3,5
b = 1,2,3
c = a + b

print(c.index(2)) #index ve a posicao do item que vc quer
print(c.count(2)) #count conta quantos itens que vc quer contar
print(c)
