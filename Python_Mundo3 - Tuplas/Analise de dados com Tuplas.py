while True:
    numero = int(input('Digite o primeiro número: '))
    outro = int(input('Digite outro número: '))
    maisum = int(input('Digite mais um número: '))
    ultimo = int(input('Digite o último número: '))
    break

numeros = numero, outro, maisum, ultimo
print(f'Você digitou os valores {numeros}')
print('---------' * 20)
print(f'O número 9 apareceu {numeros.count(9)} vez(s)') #count conta quantas vezea aparece
print(f'O número 3 apareceu na {numeros.index(3)} posição') #index mostra a posição.

