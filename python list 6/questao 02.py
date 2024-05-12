# Faça um programa que lê o sexo de 3 pessoas em uma lista, calcula e exibe a quantidade de pessoas de cada sexo

sexo = []
m = 0
f = 0

for i in range(3):
    print("Digite [M] caso você seja homem \n Digite [F] para caso você seja mulher")
    res = input("Informe o seu gênero:  ")
    sexo.append(res)

for res in sexo:
    if res == "M" or res == "m":
        m = m + 1

for res in sexo:
    if res == "F" or res == "f":
        f = f + 1


print(f"De 3 pessoas, {m} são de sexo masculino e {f} de sexo feminino")
