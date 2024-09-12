//Escreva um programa Java que leia o nome de um aluno e as notas das três provas que ele obteve no semestre. No final informar o nome do aluno e a sua média (aritmética).

import java.util.Scanner;
import java.util.concurrent.Flow.Subscriber;

public class questao03 {
    public static void main(String[] args) {
        
        System.out.println("Qual o seu nome: ");
        Scanner nomeInput = new Scanner(System.in);
        String nome = nomeInput.nextLine();

        System.out.println("Informe a sua primeira nota: ");
        Scanner n1Input = new Scanner(System.in);
        float n1 = n1Input.nextFloat();


        System.out.println("Informe a sua segunda nota: ");
        Scanner n2Input = new Scanner(System.in);
        float n2 = n2Input.nextFloat();

        System.out.println("Informe a sua terceira nota: ");
        Scanner n3Input = new Scanner(System.in);
        float n3 = n3Input.nextFloat();

        float md = (n1 + n2 + n3) / 3;

        System.out.println("O aluno: "+nome+" tem uma média aritmética de: "+md);




    }
}