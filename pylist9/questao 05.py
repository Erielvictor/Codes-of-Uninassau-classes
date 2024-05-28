# Sistema Acadêmico (Cadastro) -Faça um programa que:
#•Receba o nome e 3 notas de 4 alunos;
#•Receba o nome do arquivo a ser criado;
#•Crie um arquivo (com o nome do arquivo indicado pelo usuário) para cada aluno e escreva as informações digitadas pelo usuário no mesmo;
#oO nome deverá ficar na primeira linha do arquivo;
#oA primeira nota deverá ficar na segunda linha do arquivo, a segunda na terceira linha e a terceira na quarta; 



def cadastrar():
    arq = open(f'{nome_arq}.txt', 'w') # uma variável recebe o comando de abrir o arquivo criado
    #Note que está em F-string, pois é necessário para um bom funcionamento e identação.
    #Note também que a f-string está abrindo a variável nome_arq, ou seja, o arquivo que foi criado
    #Como a variável nome_arq representa o arquivo criado, então não é preciso especificar o nome do arquivo, basta colocar a variável que o código entende
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

    if infos[-1] == '': # Confere se tem espaço vazio 
        del infos[-1] # se tiver espaço em branco, vai apagar
        
    nomes = infos[0].split()
    notas = infos[1].split()
        

    for i in range(len(nomes)):
        print(f'Pessoa {nomes}, nota{notas}')

for i in range(4): # Esse for faz com que as funções e o input rodem 4 vezes. Deve estar antes das funções para poder funcionar corretamente.
    #Se botar esse for no início, não tem como chamar as funções dentro dele, pois o computador entende que as funções ainda não foram criadas
    nome_arq = input("Digite o nome do arquivo: ") #Pedindo o nome do arquivo

    cadastrar() #chamando as funções
    mostrar()