package teste;

public class TestaFuncionario {
    public static void main(String[] args) {
        Funcionario funcionario1 = new Funcionario(null, 0);
        
        funcionario1.setNome("João");
        funcionario1.setSalario(2500);
        
        System.out.println("Nome: " + funcionario1.getNome());
        System.out.println("Salário: " + funcionario1.getSalario());
      
    }
}
