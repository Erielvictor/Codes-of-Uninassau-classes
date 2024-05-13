# Cada  espectador  de  um  cinema  respondeu  a  um  questionário  no  qual  constava  sua opinião  em  relação  ao  filme: ótimo –3,  bom –2,  regular –1.  Faça  um  programa  que receba a opinião de 5 espectadores em uma lista, calcule e mostre:•A quantidade de pessoas que responderam ótimo;•A quantidade de pessoas que responderam bom;•A quantidade de pessoas que responderam regula

o = 0
b = 0
r = 0

o_lista = []
b_lista = []
r_lista = []


for i in range(5):
    print("Qual sua opinião sobre o filme? \n [3] para ÓTIMO \n [2] para BOM \n [3] para REGULAR")
    res = int(input("Informe a sua resposta: "))

    if res == 3:
        o_lista.append(res)
        o = o + 1
    elif res == 2:
        b_lista.append(res)
        b = b + 1
    elif res == 1:
        r_lista.append(res)
        r = r + 1
    else:
        print("Resposta inválida!")


print(f"A quantidade de pessoas que acharam o filme [ÓTIMO]] é: {o}")

print(f"A quantidade de pessoas que acharam o filme [BOM] é: {b}")

print(f"A quantidade de pessoas que acharam o filme [REGULAR] é: {r}")
