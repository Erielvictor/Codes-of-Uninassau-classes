package javalist3.AtividadeerielVictor;

import java.util.Scanner;

public class Aplicacao {
    public static void main(String[] args) {
        Scanner input = new Scanner(System.in);

        System.out.print("Digite a distância percorrida (em km): ");
        double distancia = input.nextDouble();

        System.out.print("Digite a quantidade de combustível gasto (em litros): ");
        double combustivel = input.nextDouble();

        Carro carro = new Carro(distancia, combustivel);

        double consumoMedio = carro.calcularConsumoMedio();
        System.out.printf("O consumo médio do automóvel é: %.2f km/l\n", consumoMedio);

        input.close();
    }
}
