package java list3;
import java.util.Scanner;

public class Aplicacao {
    public static void main(String[] args) {
        Scanner input = new Scanner(System.in);


        System.out.println("Digite a distância percorrida (em km): ");
        double distancia = input.nextDouble();

        System.out.println("Digite a quantidade de combustível gasto (em litros): ");
        double combustível = input.nextDouble();
        
        Carro carro = new Carro(distancia, combustível);

        double consumoMedio = carro.calcularConsumoMedio();

        System.err.printf("O consumo médio do automóvel é: %.2f km/l\n", consumoMedio);

        input.close();


    }

}
