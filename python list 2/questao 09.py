# 09 Escreva um programa para ler 3 valores e escrever a soma dos 2 maiores. Considere que o usuário não informara valores iguais

num = []

for i in range(3):
    valor = int(input(f"Informe o {i + 1}° número: ")) #pede 3 valores e printa qual a ordem(i + 1)
    num.append(valor) # adiciona os valores recebidos à lista
    num_ord = num.sort(reverse= True) #ordena a lista em ordem crescente e depois inverte(reverse = True) para a decrescente.


M_num = num[:2] 
#M-num é a variável que vai receber os maiores números
# num[:n] o n indica a quantidade de números que vão ser lidos.
#Como a ordem foi invertida, ou seja, os maiores primeiros, então se ler 2 números vai estar lendo os dois maiores.

S_M = sum(M_num)
# sum() é u serviço de soma. sum(M_num) vai somar os dois maiores números ou, se quiser, mais números. (Basta aumentar o n de range(n))

print(f"A soma dos maiores números é igual a: {S_M}")


    # Aqui não se pode usar o sorted(num) pois a variável "num_ord" não é itenerável, devido a ordenação + a reversão da ordem(de crescente vai para decrescente) para utilizar o sorted() precisaria coloca-lo antes:
    #num.append(valor)
    #new_ord = sorted(num)
    #num_ord = num.sort(reverse= True)
    # Mas isso é apenas uma dica, o código já funciona perfeitamente.