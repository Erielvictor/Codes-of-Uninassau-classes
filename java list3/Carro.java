// Escreva um programa Java para determinar o consumo médio de um automóvel sendo fornecida a distância total percorrida pelo automóvel e o total de combustível gasto.
// • Utilizar os conceitos de POO;
// • Criar duas classe: Carro() e Aplicacao()
// • Utilizar o conceito de encapsulamento: Os atributos devem ser privados;
// • Criar um método contrutor para inicializar os atributos (valores iniciais);
// • Criar um método que retorna o consumo médio;
// • consumo médio = distancia percorrida / quantidade de combustível.



/**
 * carro
 */
public class Carro {

    private double distanciaPercorrida;
    private double combustívelGasto;

    public carro(double distanciaPercorrida, double combustívelGasto) {
        this.distanciaPercorrida = distanciaPercorrida;
        this.combustívelGasto = combustívelGasto;
    }
    

    public double calcularConsumoMedio() {
        if (combustívelGasto == 0) {
            return 0; //Pra não ter divisão por zero
        }
        return distanciaPercorrida / combustívelGasto;
    }

    public double getDistanciaPercorrida() {
        return distanciaPercorrida;

    }

    public double getCombustivelGasto(){
        return combustívelGasto;
    }
}