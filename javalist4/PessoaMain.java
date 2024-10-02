package javalist4;

/**
 * Pessoa
 */
class informacoes {

    private String nome;
    private int idade;

    public informacoes(String nome, int idade){
        this.nome = nome;
        this.idade = idade;
    }

    //Getter para o atributo nome
    public String getNome(){
        return nome;
    }

    //getter para o atributo idade
    public int getIdade(){
        return idade;
    }
    
    //Setter para o atributo nome
    public void setNome(String nome){
        this.nome = nome;
    }

    //Setter para o atributo idade
    public void setIdade(int idade){
        //Validação de idade para evitar idades menores que 0

        if (idade > 0){
            this.idade = idade;
        } else{
            System.out.println("Idade inválida!");
        }
    
    }

    public void showInfo(){
        System.out.println("Nome: " + nome + ", Idade: " + idade);
    }

}

public class PessoaMain {
    
    public static void main(String[] args) {
        informacoes pessoa = new informacoes("Eriel", 19);
    
    
        //usando getters
        System.out.println("Nome: "+ pessoa.getNome());
        System.out.println("Idade: "+ pessoa.getIdade());


        //usando setters
        pessoa.setNome("Eriel");
        pessoa.setIdade(19);

        //usar a função para exibir as informações

        pessoa.showInfo();
    
    }

    
    
}