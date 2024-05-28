# Com base na questão anterior, faça um programa que faça o Cálculo de Média referindo as notas lançadas no Sistema Acadêmico, seguindo os seguintes passos:
#•Receba o nome do arquivo a ser lido;
#•Leia o arquivo indicado pelo usuário (a partir do nome do arquivo);
#•Exiba o nome do aluno, sua média no semestre e se o mesmo está aprovado ou reprovado (considere que a média da faculdade é 7,0);  

def cadastrar():
    arq = open(f'{nome_arq}.txt', 'w')
    lista_nomes = []
    lista_notas = []

    for i in range(1):
        nome = str(input("Informe o seu nome: "))
        lista_nomes.append(nome)
            
        for i in range(3):
            notas = int(input(f"Informe a sua {i + 1}° nota: "))
            lista_notas.append(notas)
            

        for i in range(1):
            arq.write(f'{lista_nomes} ')
            arq.write('\n')

        for i in range(1):
            arq.write(f"{lista_notas} ")
        arq.close()

        for i in range(1):
            s = sum(lista_notas)
            md = s / len(lista_notas)
            print(f'{md:.2f}')


for i in range(4):

    nome_arq = input("Digite o nome do arquivo: ")
    cadastrar()

   