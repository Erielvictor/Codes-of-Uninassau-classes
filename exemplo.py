idades = []
maior = 0

for x in range(3):
    idade = int(input("Digite uma idade: "))
    idades.append(idade)

for idade in idades:
    if idade > maior:
        maior = idade
        
print(maior)


