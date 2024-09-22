public class TestaFuncionario {
    public static void main(String[] args) {
        Funcionario funcionario1 = new Funcionario("João", 3000.00);
        Funcionario funcionario2 = new Funcionario("Maria", 4500.00);

        System.out.println(funcionario1);
        System.out.println("Bonificação de João: " + funcionario1.calcularBonificacao());
        
        System.out.println(funcionario2);
        System.out.println("Bonificação de Maria: " + funcionario2.calcularBonificacao());
    }
}

