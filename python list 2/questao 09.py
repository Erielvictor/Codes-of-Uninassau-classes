# 09 Escreva um programa para ler 3 valores e escrever a soma dos 2 maiores. Considere que o usuário não informara valores iguais

num = []

for i in range(5):
    valor = int(input(f"Informe o {i + 1}° número: "))
    num.append(valor)
    num_ord = num.sort(reverse= True)

M_num = num[:2]
S_M = sum(M_num)

print(f"A soma dos maiores números é igual a: {S_M}")