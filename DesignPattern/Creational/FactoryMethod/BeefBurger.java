package Creational.FactoryMethod;

public class BeefBurger implements Burger{
    @Override
    public void prepare(){
        System.out.println("Preparing beef burger...");
    }
}
