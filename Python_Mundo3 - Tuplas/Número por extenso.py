numeros = 'zero', 'um', 'dois', 'tres', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove', 'dez', 'onze', 'doze', 'treze', 'quatorze', 'quinze', 'dezesseis', 'dezessete', 'dezoito', 'dezenove', 'vinte'

while True:
    numero = int(input('Digite um número entre 0 e 20: '))
    if 0 <= numero <= 20: #se o número for menor ou igual a zero e menor e igual a 20
        break
    print('Tente novamente!')
print(f'Você digitou o número {numeros[numero]}')

