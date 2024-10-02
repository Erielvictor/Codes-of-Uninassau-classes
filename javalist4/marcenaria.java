package javalist4;

//superclassee
class movel {
    String nome;
    double tamanho;


    public movel(String nome, double tamanho){
        this.nome = nome;
        this.tamanho = tamanho;
    }

    public void montar(){
        System.out.println("O movel foi montado");
    }

    public void enviar(){
        System.out.println("O movel foi enviado");
    }
    
}

class Item extends movel{
    String modelo;

    public Item(String nome, double tamanho, String modelo){
        super(nome, tamanho);
        this.modelo = modelo;
    }

    @Override
    public void montar() {
        System.out.println("O móvel foi montado");
    }

    public void enviar(){
        System.out.println("O móvel foi enviado");
    }



}




public class marcenaria {
    public static void main(String[] args) {
        Item objeto = new Item("Baú", 2.34 , "Antigo");


        objeto.montar();
        objeto.enviar();



        System.out.println("O móvel escolhido foi: " + objeto.nome + " com o tamanho de: " + objeto.tamanho + " metros" + " sendo de modelo: " + objeto.modelo);
    }
    
}
