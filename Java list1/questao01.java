//Escreva um programa Java para determinar o consumo médio de um automóvel sendo fornecida a distância total percorrida pelo automóvel e o total de combustível gasto.

import java.util.Scanner;

public class questao01{
    public static void main(String[] args) {
        System.out.println("Informe a distância percorrida em quilometros: ");
        Scanner inputDist = new Scanner(System.in);
        int dist = inputDist.nextInt();

        System.out.println("Informe quantos litros de combustível foram gastos: ");
        Scanner inputComb = new Scanner(System.in);
        int Comb = inputComb.nextInt();


        int kml = dist / Comb;

        System.err.println("O seu carro percorre: " + kml + " quilometros por litro");

    }
}