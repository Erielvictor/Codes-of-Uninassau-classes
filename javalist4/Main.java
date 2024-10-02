package javalist4;


class Animal {

    String nome;
    int idade;


    public Animal(String nome, int idade) {
        this.nome = nome;
        this.idade = idade;
    }

    // Método da superclasse
    public void fazSom() {
        System.out.println("O animal faz um som.");
    }
}

// Subclasse
class Cao extends Animal {
    // Atributo da subclasse
    String raca;

    // Construtor da subclasse
    public Cao(String nome, int idade, String raca) {
        super(nome, idade); 
        this.raca = raca;
    }

    @Override
    public void fazSom() {
        System.out.println("O cachorro late.");
    }

    // Método específico da subclasse
    public void brinca() {
        System.out.println(nome + " está buscando a bola!");
    }
}

public class Main {
    public static void main(String[] args) {
        // Cria um objeto da subclasse
        Cao dog = new Cao("Rex", 3, "Labrador");

        // Acessa métodos da superclasse e subclasse
        dog.fazSom();  // Saída: O cachorro late.
        dog.brinca();      // Saída: Rex está buscando a bola!

        // Também pode acessar atributos herdados
        System.out.println(dog.nome + " tem " + dog.idade + " anos.");
        // Saída: Rex tem 3 anos.
    }
}
