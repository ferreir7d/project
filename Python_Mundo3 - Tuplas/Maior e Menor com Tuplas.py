from random import randint
aleatorios = (
    randint(0, 10) , randint(0, 10), randint(0, 10), randint(0, 10), randint(0, 10))

print('Os valores sorteados foram: ')

for numero in aleatorios:
    print(f'{numero}')
print(f'O maior valor sorteado foi {max(aleatorios)}') #max verifica qual é o maior valor
print(f'O menor valor sorteado foi {min(aleatorios)}') #min verific qual é o menor valor
