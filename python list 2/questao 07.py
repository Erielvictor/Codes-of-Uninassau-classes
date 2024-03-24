# 07 Escreva um algoritmo que leia 3 números inteiros e mostre o menor deles

n1 = int(input("Informe o primeiro número: "))
n2 = int(input("Informe o segundo número: "))
n3 = int(input("Informe o terceiro número: "))

lista = [n1, n2, n3]
lista_ordenada = lista.sort()


if n1 < n2 and n1 < n3:
    men = n1
    print(f"Na lista {lista} o menor número é o: {men}")

elif n2 < n1 and n2 < n3:
    men = n2
    print(f"Na lista {lista} o menor número é o: {men}")

elif n3 < n1 and n3 < n2:
    men = n3
    print(f"Na lista {lista} o menor número é o: {men}")
