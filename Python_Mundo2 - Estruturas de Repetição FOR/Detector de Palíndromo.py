frase = str(input("Digite uma frase: ")).strip().upper() #strip tira os espaços da frase, e o upper aumenta a palavra em letra maiúscula
palavra = frase.split() #split da um espaço entre as palavaras
junto = ''.join(palavra) #função join junta as palavras com espaços, ou sem, com asteriscos, ou o que você quiser.

palavrainversa = ''
for letra in range(len(junto) - 1, -1, -1):
    palavrainversa += junto[letra]
print(junto, palavrainversa)



frase1 = str(input("Digite uma frase: ")).strip().upper()
palavra1 = frase1.split()
funjuntar_palavra = '*'.join(palavra1)

palavarainvertida = ''
for letra1 in range(len(funjuntar_palavra) - 1, -1, -1):
    palavarainvertida += funjuntar_palavra[letra1]
if letra1 == funjuntar_palavra:
    print("Temos um Palíndromo")
else:
    print("A frase digitada não é um Palíndromo")

