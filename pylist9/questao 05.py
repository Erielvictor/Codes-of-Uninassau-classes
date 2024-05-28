# Sistema Acadêmico (Cadastro) -Faça um programa que:
#•Receba o nome e 3 notas de 4 alunos;
#•Receba o nome do arquivo a ser criado;
#•Crie um arquivo (com o nome do arquivo indicado pelo usuário) para cada aluno e escreva as informações digitadas pelo usuário no mesmo;
#oO nome deverá ficar na primeira linha do arquivo;
#oA primeira nota deverá ficar na segunda linha do arquivo, a segunda na terceira linha e a terceira na quarta; 



def cadastrar():
    arq = open(f'{nome_arq}.txt', 'w')
    lista_nomes = []
    lista_notas = []

    for i in range(1):
        nome = str(input("Informe o seu nome: "))
        lista_nomes.append(nome)
            
        for i in range(3):
            notas = str(input(f"Informe a sua {i + 1}° nota: "))
            lista_notas.append(notas)

        for i in range(1):
            arq.write(f'{lista_nomes} ')
            arq.write('\n')

        for i in range(1):
            arq.write(f"{lista_notas} ")
        arq.close()

def mostrar():
    arq = open(f'{nome_arq}.txt', 'r')
    dados = arq.read()

    infos = dados.split('\n')

    if infos[-1] == '': 
        del infos[-1]
        
    nomes = infos[0].split()
    notas = infos[1].split()
        

    for i in range(len(nomes)):
        print(f'Pessoa {nomes}, nota{notas}')

for i in range(4):
    nome_arq = input("Digite o nome do arquivo: ")
    cadastrar()
    mostrar()