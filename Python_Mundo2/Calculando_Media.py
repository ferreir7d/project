nota1 = float(input("Digite a sua primeira nota: "))
nota2 = float(input("Digite a sua segunda nota: "))

media = (nota1 + nota2) / 2

print("Tirando {:.1f} e {:.1f}, a média do aluno será de {:.1f}".format(nota1, nota2, media))

if media >= 7.0:
    print("A sua média foi {}, você foi APROVADO!!!".format(media))
elif media == 5.0 or 6.9:
    print("A sua média foi {}, você está de RECUPERAÇÃO!!!".format(media))
elif media < 5:
    print("A sua média foi {}, você está REPROVADO!!".format(media))

