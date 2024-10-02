package pylist9.revisão;
// Superclasse
class Animal {
    // Atributos da superclasse
    String name;
    int age;

    // Construtor da superclasse
    public Animal(String name, int age) {
        this.name = name;
        this.age = age;
    }

    // Método da superclasse
    public void makeSound() {
        System.out.println("O animal faz um som.");
    }
}

// Subclasse
class Dog extends Animal {
    // Atributo da subclasse
    String breed;

    // Construtor da subclasse
    public Dog(String name, int age, String breed) {
        super(name, age); // Chama o construtor da superclasse
        this.breed = breed;
    }

    // Sobrescreve o método da superclasse
    @Override
    public void makeSound() {
        System.out.println("O cachorro late.");
    }

    // Método específico da subclasse
    public void fetch() {
        System.out.println(name + " está buscando a bola!");
    }
}

public class Main {
    public static void main(String[] args) {
        // Cria um objeto da subclasse
        Dog dog = new Dog("Rex", 3, "Labrador");

        // Acessa métodos da superclasse e subclasse
        dog.makeSound();  // Saída: O cachorro late.
        dog.fetch();      // Saída: Rex está buscando a bola!

        // Também pode acessar atributos herdados
        System.out.println(dog.name + " tem " + dog.age + " anos.");
        // Saída: Rex tem 3 anos.
    }
}
