# 07 Escreva um algoritmo que leia 3 números inteiros e mostre o menor deles

n1 = int(input("Informe o primeiro número: "))
n2 = int(input("Informe o segundo número: "))
n3 = int(input("Informe o terceiro número: "))

lista = [n1, n2, n3] 
# para criar a lista basta escolher uma variável e por "= []" isso faz com que o pc entenda que aquela variável é uma lista. 
# A lista serve para armazenar MAIS DE UMA VARIÁVEL
lista_ordenada = lista.sort() #var.sort() faz com que os itens dentro da variável sejam ordenados em ordem crescente(Isso funciona com números e quando quer saber qual a maior palavra em quantidade de letras.)


if n1 < n2 and n1 < n3: # condicional que verifica se o n1 é o menor número. Não é necessário verificar se n2 é maior ou menor que n3, pois o quê importa é saber apenas o menor número 
    men = n1
    print(f"Na lista {lista} o menor número é o: {men}")

elif n2 < n1 and n2 < n3:
    men = n2
    print(f"Na lista {lista} o menor número é o: {men}")

elif n3 < n1 and n3 < n2:
    men = n3
    print(f"Na lista {lista} o menor número é o: {men}")

# quando printar uma das condicionais, os números serão mostrados em ordem crescente devido ao "lista.sort()"