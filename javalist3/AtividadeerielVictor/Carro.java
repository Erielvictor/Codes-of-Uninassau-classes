package javalist3.AtividadeerielVictor;

public class Carro {
    private double distanciaPercorrida;
    private double combustivelGasto;

    public Carro(double distanciaPercorrida, double combustivelGasto) {
        this.distanciaPercorrida = distanciaPercorrida;
        this.combustivelGasto = combustivelGasto;
    }

    public double calcularConsumoMedio() {
        if (combustivelGasto == 0) {
            return 0;
        }
        return distanciaPercorrida / combustivelGasto;
    }

    public double getDistanciaPercorrida() {
        return distanciaPercorrida;
    }

    public void setDistanciaPercorrida(double distanciaPercorrida) {
        this.distanciaPercorrida = distanciaPercorrida;
    }

    public double getCombustivelGasto() {
        return combustivelGasto;
    }

    public void setCombustivelGasto(double combustivelGasto) {
        this.combustivelGasto = combustivelGasto;
    }

    @Override
    public String toString() {
        return "Carro [distanciaPercorrida=" + distanciaPercorrida + ", combustivelGasto=" + combustivelGasto + "]";
    }
}