# 08 Escreva  um  algoritmo que  leia  3  números  inteiros  e  mostre  os valores  em ordem crescente.

ordem = []

for i in range(3):
    # A estrutura for x in range(n) trabalha um loop, ela roda o código de acordo com a quantidade(n) especificada.
    
    # o i é uma variável(pode ser colocado qualquer variável, vai de acordo com seu gosto),  que armazena o valor da iteração/repetição atual do looping, O valor sempre começa em 0(zero) caso não HAJA ESPECIFICAÇÃO.

    # No in range(n) o n representa quantas repetições irão acontecer. sendo que sempre acaba 1 número antes do fornecido.

    # se n = 3 então o i terá os valores de repetição: 0, 1, 2. Como dito acima, só não começa em zero quando especificado.

    num = int(input(f"Informe o {i + 1}° número: ")) 
    #{i + 1} faz o pc printar o número atual da repetição + 1
    ordem.append(num) 
    #o serviço "var.append(var2)" serve para que os valores informados sejam adicionados à variável que é uma lista.
    ord_new = sorted(ordem)
    # O serviço sorted(var) também ordena as variáveis, porém o sorted() pode ser utilizado em qualquer caso, seja tuplas, strings e dicionairos. Enquanto isso, o Sort() só pode ser usado para listas.

    # O sort() muda os valores originais da lista para o ordenado, basicamente apagando os valores antigos. Enquanto o sorted() cria uma nova lista com os valores ordenados e mantém a lista com os valores originais, permitindo que o acesso aos dados antigos.

print(f"Os valores em ordem crescente são: {ord_new}")