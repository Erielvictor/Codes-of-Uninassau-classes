# 03 Escreva  um  algoritmo  que  obtenha  dois  números  inteiros,  mostre  o  produto  e  a soma entre eles

num = [] # Cria uma lista para receber os números

for i in range(2): 
    valor = int(input(f"Digite o {i+1}º valor: "))
    num.append(valor) 
    #o serviço ".append(var)" serve para que os valores informados sejam adicionados à variável que é uma lista.

# estrutura for x in range(n) determina que o código irá repetir n vezes.
    
# No "for var" a variável(var) pode ser qualquer uma, nesse caso eu escolhi o i, mas o programador pode por qualquer uma.
    
#in range significa "No alcance" o alcance é justamente o n dentro dos (), é possível colocar qualquer número inteiro ou até mesmo uma variável que recebe a quantidade de repetições desejadas.
    
soma = sum(num) #sum() é um serviço para fazer a soma de números sem precisar usar o + ou somar itens dentro de uma lista.

print(f"A soma dos valores {num} é igual a: {soma} ")
#(f" etc {var} e {var}") é um tipo de fommatação, conhecida como: f-strings