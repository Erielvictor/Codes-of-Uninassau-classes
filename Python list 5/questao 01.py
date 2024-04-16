#Faça um programa que lê a resposta de 15 usuários para a seguinte pergunta: “Você gosta de beterraba? Digite 1 para SIM e 2 para NÃO”. Após a coleta da resposta de cada usuário, o algoritmo deverá exibir a quantidade de respostas para cada opção.


s_g = 0
n_g = 0
for i in range(15):
    print("Você gosta de beterraba? \n [1] para SIM \n [2] para NÃO")
    res = int(input("Informe a sua resposta: "))

    if res == 1:
        s_g = s_g + 1
    elif res == 2:
        n_g = n_g + 1
    else:
        print("Resposta inválida!")

print(f"A quantidade de pessoas que gostam de beterraba é: {s_g}")

print(f"A quantidade de pessoas que não gostam de beterraba é: {n_g}")