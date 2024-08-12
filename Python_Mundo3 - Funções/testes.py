def mostraLinha():
    print('*-----------------*')


mostraLinha()
print('Sou daniel')
mostraLinha()
print('Lindo')




def título(txt):
    print('-' * 30)
    print(txt)


#Programa principal
título('Daniel em vídeo')



def soma(a, b):
    s = a + b
    print(s)


# programa principal
soma(4, 5)
soma(8, 9)
soma(2, 1)


def soma(a, b ):
    print(f'valor do A = {a} e valor do B = {b}')
    print('-' * 30)
    s = a + b
    print(f'A soma A + B é {s}')


soma(4, 5)


def contador(* num):
    tam = len(num)
    print(f'Recebi os valores {num} e são ao todo {tam} números')


contador(10, 20, 30)
contador(1, 2, 3)


def dobra(lista):
    posicao = 0
    while posicao < len(lista):
        lista[posicao] *= 2
        posicao += 1


valores = [0, 2, 3, 4]
dobra(valores)
print(valores)


def soma(* valores):
    somar = 0
    for numero in valores:
        somar += numero
    print(f'Somando os valores {valores} temos {somar}')


soma(5, 2)
soma(2, 9, 4)


def somar(a=0, b=0, c=0):
    soma = a + b + c
    print(f'A soma dos números é {soma}')


somar(2, 3, )
