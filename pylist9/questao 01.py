# -Faça um programa que leia o nome de 3 pessoas, cadastrando-as em um arquivo. Em seguida, o programa deverá exibir o nome das 3 pessoas cadastra
name = []

def cadastrar(nome):
    for i in range(3):
        nome = str(input("Informe o seu nome: "))
        name.append(nome)

cadastrar(name)
print(name)