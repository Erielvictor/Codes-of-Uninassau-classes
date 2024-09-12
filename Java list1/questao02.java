//Escreva um programa Java que leia o nome de um vendedor, o seu salário fixo e o total de vendas efetuadas por ele no mês (em dinheiro). Sabendo que este vendedor ganha 15% de comissão sobre suas vendas efetuadas, informar o seu nome, o salário fixo e salário no final do mês.

import java.util.Scanner;

public class questao02 {
    public static void main(String[] args) {
        System.out.println("Qual o seu nome?\n Nome: ");
        Scanner nomeInput = new Scanner(System.in);
        String nome = nomeInput.nextLine();

        System.out.println("Informe o seu salário fixo: ");
        Scanner salInput = new Scanner(System.in);
        int sal = salInput.nextInt();

        System.out.println("Informe a quantidade de vendas feitas (em dinheiro): ");
        Scanner sellInput = new Scanner(System.in);
        int sell = sellInput.nextInt();

        double comissao = sell * 0.15;

        float salFinal = (float) (sal + comissao);

        System.out.println("O seu salário ao final do mês somado à comissão é de: R$ "+salFinal);

     }
}
