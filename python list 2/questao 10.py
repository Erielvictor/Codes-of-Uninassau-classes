#10 –Elabore um algoritmo que leia três valores que representam os três lados de um triângulo e verifique:
# a) Se o triângulo é válido
# b) Se é um triângulo equilátero, isósceles ou escaleno.
# Lembrando que: • A soma de dois lados não pode ser menor que a do terceiro lado, •
# equilátero: três lados iguais,
# •isósceles: dois lados iguais,
# • escaleno: três lados diferentes,
# • O algoritmo deve-se comunicar sempre com o usuário


l1 = float(input("Informe a medida do primeiro lado: "))
l2 = float(input("Informe a medida do segundo lado: "))
l3 = float(input("Informe a medida do terceiro lado: "))

if (l1 + l2 > l3) and (l1 + l3 > l2) and (l2 + l3 > l1):
    print("O triângulo é válido!")

    if (l1 == l2 and l2 == l3) or (l1 == l3 and l3 == l2):
        print("É um triângulo equilátero!")

    elif(l1 == l2 and l2 == l1) or (l1 == l3 and l3 == l1) or (l2 == l3 and l3 == l2):
        print("É um triângulo isósceles ")
    elif (l1 != l2 != l3):
        print("É um triângulo escaleno!")
else:
    print("O triângulo não é válido!")